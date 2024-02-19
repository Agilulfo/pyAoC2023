from advent.day03 import shared


def main():
    map = shared.load_map(__file__)
    result = 0

    for number, row, start, end in shared.extract_numbers(map):
        submap = adjacent_submap(map, row, start, end)
        if submap_has_symbol(submap):
            result += number

    print("the result is: ", result)


def adjacent_submap(full_map, row, start, end):
    submap = []

    (start_row, start_column, end_row, end_column) = adjacent_indexes(full_map, row, start, end)

    for row_index in range(start_row, end_row + 1):
        submap.append(full_map[row_index][start_column : end_column + 1])

    return submap


def adjacent_indexes(full_map, row, start, end):
    max_row = len(full_map) - 1
    max_column = len(full_map[0]) - 1

    start_row = max(0, row - 1)
    start_column = max(0, start - 1)
    end_row = min(max_row, row + 1)
    end_column = min(end + 1, max_column)

    return (start_row, start_column, end_row, end_column)



def submap_has_symbol(submap):
    for row in submap:
        for char in row:
            if not char.isdigit() and char != ".":
                return True
    return False
