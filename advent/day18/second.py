from advent.day18.parsing import parse_input


def main():
    instructions = [decode(instruction) for instruction in parse_input()]

    lake = Lake(instructions)
    # import ipdb; ipdb.set_trace()

    print(f"The lake area is: {lake.calculate_area()}")


# we can replace the decode function to test the algorithm on the smaller graph
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


class Lake:
    def __init__(self, instructions):
        distance, direction = instructions[0]
        cursor = Edge((0, 0), distance, direction)
        self.edge_count = 0
        for instruction in instructions[1:]:
            self.edge_count += 1
            next_position = cursor.end()
            distance, direction = instruction
            cursor.insert_after(Edge(next_position, distance, direction))
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
def translate_point(position, direction, distance):
    x, y = position
    match direction:
        case "U":
            return (x, y + distance)
        case "D":
            return (x, y - distance)
        case "R":
            return (x + distance, y)
        case "L":
            return (x - distance, y)


def distance(point_a, point_b):
    ax, ay = point_a
    bx, by = point_b
    if ax == bx:
        return abs(ay - by)
    elif ay == by:
        return abs(ax - bx)
    else:
        raise RuntimeError("invalid distance calculation attempt")


def opposite_direction(direction):
    match direction:
        case "U":
            return "D"
        case "D":
            return "U"
        case "R":
            return "L"
        case "L":
            return "R"


class Edge:
    def __init__(self, position, distance, direction):
        self.x, self.y = position
        self.distance = distance
        self.direction = direction
        self.next = self
        self.prev = self

    def insert_after(self, other_edge):
        former_next = self.next

        other_edge.prev = self
        other_edge.next = former_next
        self.next = other_edge
        former_next.prev = other_edge

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def start(self):
        return (self.x, self.y)

    def end(self):
        return translate_point(self.start(), self.direction, self.distance)

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

    def is_buldge(self, cw):
        return cw == self.cw_segment() and cw == self.prev.cw_segment()

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return f"Edge: {self.x}, {self.y} - {self.direction} {self.distance}"
