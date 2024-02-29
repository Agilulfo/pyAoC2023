from advent.day10.parsing import load_map
from advent.day11.first import discover_galaxies, find_expansions, distances


def main():
    universe = load_map(file_path=__file__)
    # print_map(universe)
    galaxies = discover_galaxies(universe)
    expanding_rows, expanding_columns = find_expansions(universe)

    print(
        distances(
            galaxies, expanding_rows, expanding_columns, expansion_multiplier=999999
        )
    )
