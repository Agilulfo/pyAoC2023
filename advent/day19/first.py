from advent.day19.parsing import parse_input


def main():
    workflows, parts = parse_input()

    workflows_map = {}
    for workflow in workflows:
        name, rules, default = workflow
        rules = [
            Rule(category, comparator, value, destination)
            for category, comparator, value, destination in rules
        ]
        workflows_map[name] = Workflow(name, rules, default)

    parts = [Part(x, m, a, s) for x, m, a, s in parts]
    for part in parts:
        destination = "in"
        while True:
            workflow = workflows_map[destination]
            destination = workflow.apply(part)
            match destination:
                case "A":
                    part.approve()
                    break
                case "R":
                    part.reject()
                    break

    total_rating = 0
    for part in parts:
        total_rating += part.rating()

    print(f"total_rating is {total_rating}")


class Rule:
    def __init__(self, category, comparator, value, destination):
        self.category = category
        self.comparator = comparator
        self.value = int(value)
        self.destination = destination

    def apply(self, part):
        return self._comp_func()(part.__getattribute__(self.category), self.value)

    def _comp_func(self):
        match self.comparator:
            case ">":
                return int.__gt__
            case "<":
                return int.__lt__


class Workflow:
    def __init__(self, name, rules, default):
        self.name = name
        self.rules = rules
        self.default = default

    def apply(self, part):
        destination = self.default
        for rule in self.rules:
            if rule.apply(part):
                destination = rule.destination
                break
        return destination


class Part:
    def __init__(self, x, m, a, s):
        self.x = int(x)
        self.m = int(m)
        self.a = int(a)
        self.s = int(s)
        self.approved = None

    def rating(self):
        if self.approved:
            return self.x + self.m + self.a + self.s
        else:
            return 0

    def approve(self):
        self.approved = True

    def reject(self):
        self.approved = False
