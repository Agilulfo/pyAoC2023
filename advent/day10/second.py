from advent.day10.parsing import load_map
from advent.day10.shared import find_start, explore_loop, Aggregator, go

def main():
    map = load_map()
    map = [list(line) for line in map]
    print_map(map)
    print()
    start = find_start(map)

    first = FirstPass()
    explore_loop(map, start, first)

    second = SecondPass(first.pipe_set, first.visited_clockwise(), map)
    explore_loop(map, start, second)

    first.color_map(map)
    print_map(map)
    print()
    color_gaps(first.pipe_set, second.enclosed_locations, map)
    second.color_map(map)
    print_map(map)

    print(len(second.enclosed_locations))

CLOCKWISE_INCREMENT = {
    "-": {"R": 0, "L": 0},
    "S": {"R": 0, "L": 0},
    "|": {"U": 0, "D": 0},
    "F": {"U": 1, "L": -1},
    "7": {"R": 1, "U": -1},
    "J": {"D": 1, "R": -1},
    "L": {"D": -1, "L": 1}
}

def color_gaps(pipes, inside, map):
    for location in list(inside):
        next, _value = go(map, location, "R")
        while next not in inside and next not in pipes:
            inside.add(next)
            next, _value= go(map, next, "R")


class FirstPass(Aggregator):
    def __init__(self):
        # Database of pieces that are part fo the loop
        self.pipe_set = set()
        self.clockwise_index = 0

    def collect(self, new_position, new_value, old_position, old_value, direction):
        self.pipe_set.add(old_position)
        self.clockwise_index += CLOCKWISE_INCREMENT[new_value][direction]

    def visited_clockwise(self):
        return self.clockwise_index > 0

    def color_map(self, map):
        for row, line in enumerate(map):
            for column, char in enumerate(line):
                if (row, column) in self.pipe_set:
                    map[row][column] = " "


# true clockwise
ENCLOSED_NEIGHBOURS = {
    "-": {"R": {True: ["D"], False: ["U"]}, "L": {True: ["U"], False: ["D"]}},
    "S": {"R": {True: [], False: []}, "L": {True: [], False: []},"U": {True: [], False: []}, "D": {True: [], False: []}}, # not entirelly accurate but might work for my input
    "|": {"U": {True: ["R"], False: ["L"]}, "D": {True: ["L"], False: ["R"]}},
    "F": {"U": {True: [], False: ["L", "U"]}, "L": {True: ["U", "L"], False: []}},
    "7": {"R": {True: [], False: ["U", "R"]}, "U": {True: ["U", "R"], False: []}},
    "J": {"R": {True: ["D", "R"], False: []}, "D": {True: [], False: ["D", "R"]}},
    "L": {"D": {True: ["L", "D"], False: []}, "L": {True: [], False: ["L", "D"]}}
}

class SecondPass(Aggregator):
    def __init__(self, pipe_set, clockwise_visit, map):
        self.pipe_set = pipe_set
        self.clockwise_visit = clockwise_visit
        self.enclosed_locations = set()
        self.map = map

    def collect(self, new_position, new_value, old_position, old_value, direction):
        check_directions = ENCLOSED_NEIGHBOURS[new_value][direction][self.clockwise_visit]
        for direction in check_directions:
            destination, _value = go(self.map, new_position, direction)
            if destination not in self.pipe_set:
                self.enclosed_locations.add(destination)


    def color_map(self, map):
        for row, line in enumerate(map):
            for column, char in enumerate(line):
                if (row, column) in self.enclosed_locations:
                    map[row][column] = "#"


def print_map( map):
        for row, line in enumerate(map):
            for column, char in enumerate(line):
                if column == 0:
                    print("\n", end = "")
                print(char, end = "")
