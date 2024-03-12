from advent.day10.parsing import load_map
from advent.day16.contraption import Contraption


def main():
    map = load_map(__file__)
    contraption = Contraption(map)

    max_energy_power = 0

    rows = len(map)
    columns = len(map[0])

    for row_index in range(rows):
        contraption.energize("E", row_index, 0)
        max_energy_power = max(max_energy_power, contraption.count_energized_tiles())

        contraption.energize("W", row_index, columns - 1)
        max_energy_power = max(max_energy_power, contraption.count_energized_tiles())

    for column_index in range(columns):
        contraption.energize("S", 0, column_index)
        max_energy_power = max(max_energy_power, contraption.count_energized_tiles())

        contraption.energize("N", rows - 1, column_index)
        max_energy_power = max(max_energy_power, contraption.count_energized_tiles())

    print(f"the energy level is {max_energy_power}")
