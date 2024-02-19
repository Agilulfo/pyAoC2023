from advent.day03 import shared


def main():
    map = shared.load_map(__file__)
    numbers = shared.extract_numbers(map)
    gears = extract_gears(map)
    result = 0

    for number in numbers:
        for gear in adjacent_gears(map, number):
            gears[gear].append(number[0])

    for ratio in gears.values():
        if len(ratio) == 2:
            a, b = ratio
            result += a * b

    print("the result is: ", result)


def extract_gears(map):
    gears = {}
    for row_index in range(len(map)):
        line_lenght = len(map[row_index])
        for column_index in range(line_lenght):
            char = map[row_index][column_index]
            if char == "*":
                gears[(row_index, column_index)] = []
    return gears


def adjacent_gears(map, number):
    found_gears = []
    (_, row, start, end) = number

    (start_row, start_column, end_row, end_column) = shared.adjacent_indexes(
        map, row, start, end
    )

    for row_index in range(start_row, end_row + 1):
        for column_index in range(start_column, end_column + 1):
            if map[row_index][column_index] == "*":
                found_gears.append((row_index, column_index))

    return found_gears
