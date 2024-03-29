from advent.day13.parsing import parse_input
from advent.day13.pattern import Pattern


def main():
    patterns = parse_input()
    patterns = [Pattern(pattern) for pattern in patterns]
    counter = 0
    for pattern in patterns:
        row_simmetry, index = pattern.get_primary_simmetry()
        index += 1
        if row_simmetry:
            counter += 100 * index
        else:
            counter += index
    print(f"the sum is: {counter}")
