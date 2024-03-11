from advent.day10.parsing import load_map
from advent.day14.platform import Platform, NUMBER_OF_CYCLES


def main():
    platform = Platform(load_map(file_path=__file__))
    prediction = platform.spin_and_weight(NUMBER_OF_CYCLES)
    print(f"the total weight is: {prediction}")
