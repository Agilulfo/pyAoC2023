from advent import utils

def main():
    map = load_map(utils.input_path(__file__))


def load_map(file_path):
    with open(utils.input_path(__file__)) as input:
         return input.readlines()


def extract_numbers(map):
    buffer = None
#     row_index = None
    start = None
    numbers = []

    for row_index  in range(len(map)):
        line_lenght = len(map[row_index])
        for column_index in range(line_lenght):
            char = map[row_index][column_index]
            if char.isdigit():
                if start:
                    buffer = buffer + char
                else:
                    start = column_index
                    buffer = char
            else:
                if start:
                    numbers.append((int(buffer), row_index, start, column_index - 1))
                    start = None
                    buffer = None

    return numbers
