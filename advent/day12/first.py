from advent.day12.parsing import parse_input
from advent.day12.records import count_arrangements


def main():
    records = parse_input()
    arrangements = 0

    for a, b in records:
        arrangements += count_arrangements(a, tuple(b))
    print(f"Total number of arrangements is {arrangements}")
