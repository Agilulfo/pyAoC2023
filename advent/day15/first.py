from advent.utils import input_path
from advent.day15.hash import hash


def main():
    with open(input_path(__file__)) as input:
        instructions = input.readline()[:-1].split(",")

    hashes = [hash(instruction) for instruction in instructions]
    print(f"hash sum is: {sum(hashes)}")
