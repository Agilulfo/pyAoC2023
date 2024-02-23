from advent import utils
import functools


def main():
    time, distance = parse_input()
    races = list(zip(time, distance))
    margins = [race_margin(race) for race in races]
    total_margin = functools.reduce(lambda x, y: x * y, margins)
    print(f"margin is: {total_margin}")



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


def race_margin(race):
    time, max_distance = race

    margin = 0
    for hold_time in range(1, time):
        distance = calculate_distance(time, hold_time)
        if distance > max_distance:
            margin += 1
    return margin


def calculate_distance(time_limit, hold_time):
    assert hold_time < time_limit
    speed = hold_time
    time_to_move = time_limit - hold_time
    distance = speed * time_to_move
    return distance
