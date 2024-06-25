from advent.day20.parsing import parse_input
from collections import deque


def main():
    setup = parse_input()
    broker = Broker()
    button = Button(broker)
    module_map = init_modules(setup, broker)
    broker.set_module_map(module_map)

    for _ in range(1000):
        button.press()

    print(f"The output is: {broker.low_counter * broker.high_counter}")


def init_modules(setup, broker):
    module_map = {}
    for module_description in setup:
        name, outputs = module_description
        if name == "broadcaster":
            module_map[name] = Broadcaster("broadcaster", outputs, broker)
        elif name[0] == "%":
            module_map[name[1:]] = FlipFlop(name[1:], outputs, broker)
        elif name[0] == "&":
            module_map[name[1:]] = Conjunction(name[1:], outputs, broker)

    for module in module_map.values():
        module.input_discovery(module_map)

    return module_map


class Broker:
    def __init__(self):
        self.low_counter = 0
        self.high_counter = 0
        self.queue = deque()

    def post(self, sender, level, recipients):
        for recipient in recipients:
            self.queue.append((sender, level, recipient))
            # print(f"{sender} {level} to {recipient}, {len(self.queue)}")
        match level:
            case "high":
                self.high_counter += len(recipients)
            case "low":
                self.low_counter += len(recipients)

    def process(self):
        if len(self.queue) > 0:
            sender, level, recipient = self.queue.popleft()
            recipient = self.module_map.get(recipient)
            if recipient:
                recipient.receive_signal(sender, level)
            return True
        return False

    def set_module_map(self, module_map):
        self.module_map = module_map


class BaseModule:
    def __init__(self, name, outputs, broker):
        self.name = name
        self.outputs = outputs
        self.broker = broker

    def receive_signal(self, sender, level):
        raise NotImplementedError

    def input_discovery(self, module_map):
        for output in self.outputs:
            output_module = module_map.get(output)
            if output_module:
                output_module.add_input(self.name)

    def add_input(self, name):
        pass


class Button:
    def __init__(self, broker):
        self.broker = broker

    def press(self):
        self.broker.post("button", "low", ["broadcaster"])
        while self.broker.process():
            pass


class Broadcaster(BaseModule):
    def receive_signal(self, _sender, level):
        self.broker.post(self.name, level, self.outputs)


class FlipFlop(BaseModule):
    def __init__(self, name, outputs, broker):
        super().__init__(name, outputs, broker)
        self.is_on = False

    def receive_signal(self, _sender, level):
        if level == "low":
            self.is_on = not self.is_on
            if self.is_on:
                output_level = "high"
            else:
                output_level = "low"
            self.broker.post(self.name, output_level, self.outputs)


class Conjunction(BaseModule):
    def __init__(self, name, outputs, broker):
        super().__init__(name, outputs, broker)
        self.memory = {}

    def update_memory(self, sender, level):
        self.memory[sender] = level

    def are_all_high(self):
        for level in self.memory.values():
            if level == "low":
                return False
        return True

    def add_input(self, name):
        self.memory[name] = "low"

    def receive_signal(self, sender, level):
        self.update_memory(sender, level)
        if self.are_all_high():
            output_level = "low"
        else:
            output_level = "high"
        self.broker.post(self.name, output_level, self.outputs)
