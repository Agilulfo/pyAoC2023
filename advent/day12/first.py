from advent.day12.parsing import parse_input
from advent.day12.records import ConditionRecord
import logging


def main():
    records = parse_input()
    arrangements = 0

    for a, b in records:
        record = ConditionRecord(a, b)
        try:
            arrangements += record.count_arrangements()
        except NotImplementedError:
            logging.info(f"\nReduced    {a} <- {b}\nonly up to {record}")
            pass
    print(f"Total number of arrangements is {arrangements}")
