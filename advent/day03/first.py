from advent import utils

def main():
    map = load_map(utils.input_path(__file__))
    result = 0

    for number, row, start, end in extract_numbers(map):
        submap = adjacent_submap(map, row, start, end)
        if submap_has_symbol(submap):
            result += number

    print("the result is: ", result)


def load_map(file_path):
    with open(utils.input_path(__file__)) as input:
         return input.read().splitlines()

def extract_numbers(map):
    numbers = []

    buffer = None
    start = None

    for row_index  in range(len(map)):
        line_lenght = len(map[row_index])
        for column_index in range(line_lenght):
            char = map[row_index][column_index]
            last_char = column_index == line_lenght - 1
            if char.isdigit():
                if buffer:
                    buffer += char
                else:
                    start = column_index
                    buffer = char

                if last_char:
                    numbers.append((int(buffer), row_index, start, column_index))
                    start = None
                    buffer = None

            else:
                if buffer:
                    numbers.append((int(buffer), row_index, start, column_index - 1))
                    start = None
                    buffer = None

    return numbers

def adjacent_submap(full_map, row, start, end):
    max_row = len(full_map) - 1
    max_column = len(full_map[0]) - 1

    submap = []

    start_row = max( 0 , row - 1)
    start_column = max(0 , start - 1)
    end_row = min ( max_row, row + 1)
    end_column = min( end + 1, max_column )

    for row_index in range(start_row, end_row + 1):
        submap.append(full_map[row_index][start_column:end_column + 1])

    return submap

def submap_has_symbol(submap):
    for row in submap:
        for char in row:
            if not char.isdigit() and char != ".":
                return True
    return False
