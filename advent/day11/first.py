from advent.day10.parsing import load_map
import bisect


def main():
    universe = load_map(file_path=__file__)
    # print_map(universe)
    galaxies = discover_galaxies(universe)
    expanding_rows, expanding_columns = find_expansions(universe)

    print(distances(galaxies, expanding_rows, expanding_columns))


def discover_galaxies(universe):
    galaxies = []
    for row_index, row in enumerate(universe):
        for column_index, cell in enumerate(row):
            if cell == "#":
                galaxies.append((row_index, column_index))
    return galaxies


def distances(galaxies, expanding_rows, expanding_galaxies, expansion_multiplier=1):
    total_distance = 0
    for index, galaxy in enumerate(galaxies):
        for destination_galaxy in galaxies[index + 1 :]:
            total_distance += distance(
                galaxy,
                destination_galaxy,
                expanding_rows,
                expanding_galaxies,
                expansion_multiplier,
            )
    return total_distance


# could be done as part of discover_galaxies.. but whatever!
def find_expansions(universe):
    expanding_columns = set(range(len(universe[0])))
    expanding_rows = []

    for row_index, row in enumerate(universe):
        empty_row = True
        for column_index, cell in enumerate(row):
            if cell == "#":
                expanding_columns.discard(column_index)
                empty_row = False
        if empty_row:
            expanding_rows.append(row_index)
    return expanding_rows, sorted(list(expanding_columns))


# to avoid
#   1 2 3 4
# 1   x x x
# 2     x x
# 3       x
# 4


def distance(
    galaxy_a, galaxy_b, expanding_rows, expanding_columns, expansion_multiplier
):
    expansions = expansions_between(
        galaxy_a, galaxy_b, expanding_rows, expanding_columns
    )
    return (
        abs(galaxy_a[0] - galaxy_b[0])
        + abs(galaxy_a[1] - galaxy_b[1])
        + expansions * expansion_multiplier
    )


def expansions_between(galaxy_a, galaxy_b, expanding_rows, expanding_columns):
    a_row, a_column = galaxy_a
    b_row, b_column = galaxy_b
    rows = abs(
        bisect.bisect(expanding_rows, a_row) - bisect.bisect(expanding_rows, b_row)
    )
    columns = abs(
        bisect.bisect(expanding_columns, a_column)
        - bisect.bisect(expanding_columns, b_column)
    )
    return rows + columns
