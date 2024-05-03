from advent import utils

# after inspecting the input I've found out that
# the path expand in all four quadrans of the plane
# if we start from point 0,0


def main():
    instructions = parse_input()

    x, y = 0, 0

    for direction, distance, _ in instructions:
        print(f"exectuing instruction: {direction} {distance} on {x} {y}")
        match direction:
            case "U":
                y = y - distance
            case "D":
                y = y + distance
            case "R":
                x = x + distance
            case "L":
                x = x - distance
        print(f"point {x}, {y}")
        # if x < 0 or Y < 0:
        #     raise RuntimeError("omg")


def parse_input():
    with open(utils.input_path(__file__)) as input:
        return [unpack_line(line) for line in input]


def unpack_line(line):
    direction, distance, color = line.split(" ")
    distance = int(distance)
    color = color[2:-2]
    return (direction, distance, color)
