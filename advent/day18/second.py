from advent.day18.parsing import parse_input


def main():
    instructions = [decode_wrongly(instruction) for instruction in parse_input()]
    lake = Lake(instructions)
    print(f"The lake area is: {lake.calculate_area()}")


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


def decode_wrongly(instruction):
    direction, distance, _ = instruction
    return (distance, direction)


class Lake:
    def __init__(self, instructions):
        distance, direction = instructions[0]
        cursor = Edge((0, 0), distance, direction, self, 1)
        self.edge_count = 1
        for instruction in instructions[1:]:
            self.edge_count += 1
            next_position = cursor.end()
            distance, direction = instruction
            cursor.insert_after(
                Edge(next_position, distance, direction, self, self.edge_count)
            )
            cursor = cursor.next

        self.cursor = cursor.next
        self._identify_direction()

    def removing_edge(self, edge):
        if self.cursor == edge:
            self.cursor = edge.next
        self.edge_count -= 1

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
        area = 0

        while self.edge_count > 4:
            edge = self.pick_chop_edge()

            chop_distance = min(edge.prev.distance, edge.next.distance)
            chop_direction = opposite_direction(edge.prev.direction)

            area_increment = (edge.distance + 1) * chop_distance
            area += area_increment
            edge.prev.shift_end(chop_direction, chop_distance)
            edge.shift_start(chop_direction, chop_distance)
            edge.next.shift_start(chop_direction, chop_distance)

            if (
                edge.direction == edge.prev.direction
                or edge.direction == opposite_direction(edge.prev.direction)
            ):
                edge.shift_start(
                    opposite_direction(edge.prev.direction), edge.prev.distance
                )
                edge.prev.shift_end(
                    opposite_direction(edge.prev.direction), edge.prev.distance
                )

            if (
                edge.direction == edge.next.direction
                or edge.direction == opposite_direction(edge.next.direction)
            ):
                edge.shift_end(edge.next.direction, edge.next.distance)
                edge.next.shift_start(edge.next.direction, edge.next.distance)

        return area + (self.cursor.distance + 1) * (self.cursor.next.distance + 1)

    def pick_chop_edge(self):
        tmp_cursor = self.cursor

        candidate = None

        first_loop = True
        while tmp_cursor != self.cursor or first_loop:
            if tmp_cursor.is_buldge(self.cw):
                if candidate is None or tmp_cursor < candidate:
                    candidate = tmp_cursor
            tmp_cursor = tmp_cursor.next
            first_loop = False

        return candidate


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
    def __init__(self, position, distance, direction, lake, identifier):
        self.x, self.y = position
        self.distance = distance
        self.direction = direction
        self.next = self
        self.prev = self
        self.lake = lake
        self.identifier = identifier

    def insert_after(self, other_edge):
        former_next = self.next

        other_edge.prev = self
        other_edge.next = former_next
        self.next = other_edge
        former_next.prev = other_edge

    def remove(self):
        self.lake.removing_edge(self)
        self.prev.next = self.next
        self.next.prev = self.prev

    def start(self):
        return (self.x, self.y)

    def end(self):
        return translate_point(self.start(), self.direction, self.distance)

    def shift_start(self, direction, distance):
        self.x, self.y = translate_point(self.start(), direction, distance)
        if direction == self.direction:
            self.distance = self.distance - distance
        elif direction == opposite_direction(self.direction):
            self.distance = self.distance + distance
        self.significance_check()

    def shift_end(self, direction, distance):
        if direction == self.direction:
            self.distance = self.distance + distance
        elif direction == opposite_direction(self.direction):
            self.distance = self.distance - distance
        else:
            self.x, self.y = translate_point(self.start(), direction, distance)
        self.significance_check()

    def significance_check(self):
        if self.distance == 0:
            self.remove()

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
        end_x, end_y = self.end()
        return f"Edge #{self.identifier}: {self.x}, {self.y} - {self.direction} {self.distance} - {end_x}, {end_y}"
