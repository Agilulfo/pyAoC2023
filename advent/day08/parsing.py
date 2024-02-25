from advent import utils


def parse_input():
    with open(utils.input_path(__file__)) as input:
        directions = input.readline()[:-1]
        input.readline()
        nodes = [parse_line(line) for line in input]
        return directions, nodes


def parse_line(line):
    return (line[0:3], line[7:10], line[12:15])
