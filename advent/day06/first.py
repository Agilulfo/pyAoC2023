from advent import utils


def main():
    time, distance = parse_input()
    races = list(zip(time, distance))
    print(races)


def parse_input():
    with open(utils.input_path(__file__)) as input:
        lines = input.readlines()
        time = extract_numbers(lines[0])
        distance = extract_numbers(lines[1])
        return time, distance


def extract_numbers(line):
    _, number_list = line.split(":")
    numbers = [int(number) for number in number_list.split(" ") if len(number) > 1]
    return numbers
