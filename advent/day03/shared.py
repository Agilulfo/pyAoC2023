from advent import utils


def load_map(file_path):
    with open(utils.input_path(__file__)) as input:
        return input.read().splitlines()


def extract_numbers(map):
    numbers = []

    buffer = None
    start = None

    for row_index in range(len(map)):
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
