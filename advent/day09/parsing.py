from advent import utils


def parse_input():
    with open(utils.input_path(__file__)) as input:
        return [[int(number) for number in line.split(" ")] for line in input]
