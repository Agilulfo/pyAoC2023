from advent.day12.parsing import parse_input
from advent.day12.records import ConditionRecord


def main():
    records = parse_input()
    arrangements = 0

    for a, b in records:
        arrangements += ConditionRecord(a, b).count_arrangements()

    print(f"Total number of arrangements is {arrangements}")
