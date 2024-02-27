ENDS = {
    "-": ["R", "L"],
    "|": ["R", "L"],
    "F": ["D", "L"],
    "7": ["D", "R"],
    "J": ["U", "L"],
    "L": ["U", "R"],
}

OPPOSITE = {"L": "R", "R": "L", "U": "D", "D": "U"}

# direction where to continue
CONTINUE = {
    "-": {"R": "R", "L": "L"},
    "|": {"U": "U", "D": "D"},
    "F": {"U": "R", "L": "D"},
    "7": {"R": "D", "U": "L"},
    "J": {"D": "L", "R": "U"},
    "L": {"D": "R", "L": "U"},
}

def follow_loop(map, start, direction):
    cursor = start
    value = None

    counter = 0
    while True:
        counter += 1
        cursor, value = go(map, cursor, direction)
        if value == "S":
            break
        direction = CONTINUE[value][direction]
    return counter


def find_start(map):
    for row, line in enumerate(map):
        for column, char in enumerate(line):
            if char == "S":
                return (row, column)


def go(map, origin, direction):
    row, column = origin

    destination = None
    match direction:
        case "R":
            destination = (row, column + 1)
        case "L":
            destination = (row, column - 1)
        case "U":
            destination = (row - 1, column)
        case "D":
            destination = (row + 1, column)

    try:
        row, column = destination
        return destination, map[row][column]
    except KeyError:
        raise OutOfMapError


class OutOfMapError(Exception):
    pass


def explore_loop(map, start):
    for direction in ["R", "D", "L", "U"]:
        try:
            position, value = go(map, start, direction)
            if value in ENDS.keys() and OPPOSITE[direction] in ENDS[value]:
                return follow_loop(map, start, direction)
        except OutOfMapError:
            pass
