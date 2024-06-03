from advent import utils


def parse_input():
    with open(utils.input_path(__file__)) as input:
        return [unpack_line(line) for line in input]


def unpack_line(line):
    direction, distance, color = line.split(" ")
    distance = int(distance)
    color = color[2:-2]
    return (direction, distance, color)
