from advent.day10.parsing import load_map
from advent.day16.contraption import Contraption

def main():
    map = load_map(__file__)
    contraption = Contraption(map)
    contraption.energize()
    # print(contraption)
    print(f"the energy level is {contraption.count_energized_tiles()}")
