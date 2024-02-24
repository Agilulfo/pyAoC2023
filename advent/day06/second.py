from advent.day06 import first


def main():
    time, distance = first.parse_input()
    time = fix_kerning(time)
    distance = fix_kerning(distance)

    # well.. it works, it takes a couple of seconds to run but it runs
    print(f"Race margin is {first.race_margin((time, distance))}")


def fix_kerning(numbers):
    return int("".join([str(number) for number in numbers]))
