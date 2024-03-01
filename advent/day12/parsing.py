from advent.utils import input_path


def parse_input():
    with open(input_path(__file__)) as input:
        return [parse_line(line) for line in input]


def parse_line(line):
    condition_record, sequences = line.split(" ")
    sequences = [int(sequence) for sequence in sequences.split(",")]

    return condition_record, sequences
