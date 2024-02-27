from advent.day10.parsing import load_map
from advent.day10.shared import find_start, explore_loop


def main():
    map = load_map()
    start = find_start(map)
    length = explore_loop(map, start)
    print(f"Farthest distance is {length//2}")
