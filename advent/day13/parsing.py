from advent.utils import input_path


def parse_input():
    patterns = []
    with open(input_path(__file__)) as input:
        current_pattern = []
        for row in input:
            if row == "\n":
                patterns.append(current_pattern)
                current_pattern = []
            else:
                current_pattern.append(row[:-1])
        patterns.append(current_pattern)
    return patterns
