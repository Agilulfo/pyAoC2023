from advent.day10.parsing import load_map
from advent.day10.shared import find_start, explore_loop, StepCounter


def main():
    map = load_map()
    start = find_start(map)
    counter = StepCounter()
    explore_loop(map, start, counter)
    print(f"Farthest distance is {counter.counter//2}")
