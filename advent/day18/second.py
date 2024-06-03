from advent.day18.parsing import parse_input


def main():
    instructions = [decode(instruction) for instruction in parse_input()]

    loop = Loop(instructions)
    # import ipdb; ipdb.set_trace()

    print(f"The lake area is: {loop.calculate_area()}")


def decode(instruction):
    _, _, code = instruction
    distance = int(code[:-1], 16)
    match code[-1]:
        case "0":
            direction = "R"
        case "1":
            direction = "D"
        case "2":
            direction = "L"
        case "3":
            direction = "U"
    return (distance, direction)


class Loop:
    def __init__(self, instructions):
        cursor = Edge((0, 0), instructions[0])
        for instruction in instructions[1:]:
            next_position = cursor.end()
            cursor.insert_after(Edge(next_position, instruction))
            cursor = cursor.next

        self.cursor = cursor.next
        self._identify_direction()

    def _identify_direction(self):
        tmp_cursor = self.cursor

        cw_counter = 0
        while tmp_cursor.next != self.cursor:
            if tmp_cursor.cw_segment():
                cw_counter += 1
            else:
                cw_counter -= 1
            tmp_cursor = tmp_cursor.next

        self.cw = cw_counter > 0

    def calculate_area(self):
        return 10


class Edge:
    def __init__(self, position, instruction):
        self.x, self.y = position
        self.distance, self.direction = instruction
        self.next = self
        self.prev = self

    def insert_after(self, other_edge):
        former_next = self.next

        other_edge.prev = self
        other_edge.next = former_next
        self.next = other_edge
        former_next.prev = other_edge

    def end(self):
        match self.direction:
            case "U":
                return (self.x, self.y + self.distance)
            case "D":
                return (self.x, self.y - self.distance)
            case "R":
                return (self.x + self.distance, self.y)
            case "L":
                return (self.x - self.distance, self.y)

    def cw_segment(self):
        sequence = (self.direction, self.next.direction)
        match sequence:
            case ("U", "R"):
                return True
            case ("U", "L"):
                return False
            case ("D", "R"):
                return False
            case ("D", "L"):
                return True
            case ("L", "D"):
                return False
            case ("L", "U"):
                return True
            case ("R", "D"):
                return True
            case ("R", "U"):
                return False

    def __repr__(self):
        return f"Edge: {self.x}, {self.y} - {self.direction} {self.distance}"
