from advent.day10.parsing import load_map
from advent.day14.platform import Platform

def main():
    platform = Platform(load_map(file_path=__file__))
    platform.tilt("N")
    print(f"the total weight is: {platform.get_weight()}")
