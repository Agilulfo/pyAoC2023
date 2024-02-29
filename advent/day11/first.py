from advent.day10.parsing import load_map


def main():
    universe = load_map(file_path=__file__)
    # print_map(universe)
    galaxies = discover_galaxies(universe)
    print(distances(galaxies))


def discover_galaxies(universe):
    galaxies = []
    for row_index, row in enumerate(universe):
        for column_index, cell in enumerate(row):
            if cell == "#":
                galaxies.append((row_index, column_index))
    return galaxies


def distances(galaxies):
    total_distance = 0
    for index, galaxy in enumerate(galaxies):
        for destination_galaxy in galaxies[index + 1 :]:
            total_distance += distance(galaxy, destination_galaxy)
    return total_distance


#   1 2 3 4
# 1   x x x
# 2     x x
# 3       x
# 4


def distance(galaxy_a, galaxy_b):
    return abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])
