from advent.utils import input_path
from advent.day15.hash import hash as custom_hash
from functools import cached_property


def main():
    with open(input_path(__file__)) as input:
        instructions = input.readline()[:-1].split(",")

    hashmap = Initiation(instructions)
    hashmap.run()

#HASHMAP
class Initiation:
    def __init__(self, instructions):
        self.instructions = instructions
        self.boxes = [Box(index) for index in range(256)]

    def run(self):
        for instruction in self.instructions:
            op = Operation(instruction)
            box = self.boxes[op.box_id]
            box.tweak(op)

        import pprint
        for box in self.boxes:
            pprint.pprint(box)


class Operation:
    def __init__(self, instruction):
        self.instruction = instruction
        if self.instruction[-1] == "-":
            self.lens_id = self.instruction[:-1]
            self.action = "-"
        else:
            self.lens_id = self.instruction[:-2]
            self.action = (self.instruction[-2], self.instruction[-1])

    @cached_property
    def box_id(self):
        return custom_hash(self.instruction)


class Box:
    def __init__(self, index):
        self.index = index
        self.lens_list = []
        self.lens_set = set()

    def tweak(self, operation):
        match operation.action:
            case "-":
                self.remove_lens(operation.lens_id)
            case ("=", focal_length) :
                self.add_lens(Lens(operation.lens_id, focal_length))

    def add_lens(self, lens):
        if lens.lens_id in self.lens_set:
            return
        self.lens_list.append(lens)
        self.lens_set.add(lens.lens_id)

    def remove_lens(self, lens_id):
        if not lens_id in self.lens_set:
            return
        for index, lens in self.lens_list:
            if lens.lens_id == lens_id:
                self.lens_list.pop(index)
                break
        self.lens_set.remove(lens_id)

    def __repr__(self):
        return f"Box {self.index} - {self.lens_list}"

class Lens:
    def __init__(self, lens_id, focal_length):
        self.lens_id = lens_id
        self.focal_length = focal_length

    def __hash__(self):
        return hash(self.lens_id)

    def __repr__(self):
        return f"{self.lens_id}, {self.focal_length}"
