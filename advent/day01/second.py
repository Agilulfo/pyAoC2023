word_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def main():
    with open("./advent/day01/input") as input:
        calibration_value = 0
        for line in input:
            calibration_value += extract_number(line)
        print("the calibration_value is {0}".format(calibration_value))


def extract_number(line):
    return join_digits(find_first_number(line), find_last_number(line))


def find_first_number(line):
    if line[0].isdigit():
        return int(line[0])

    word = None
    for number in word_map.keys():
        if start_with(line, number):
            word = number
            break

    if word:
        return word_map[word]

    return find_first_number(line[1:])


def find_last_number(line):
    if line[-1].isdigit():
        return int(line[-1])

    word = None
    for number in word_map.keys():
        if end_with(line, number):
            word = number
            break

    if word:
        return word_map[word]

    return find_last_number(line[:-1])


def start_with(line, word):
    if can_contain(line, word):
        return line[: len(word)] == word
    return False


def end_with(line, word):
    if can_contain(line, word):
        return line[-len(word) :] == word
    return False


def can_contain(line, word):
    return len(line) >= len(word)


def join_digits(a, b):
    return a * 10 + b


if __name__ == "__main__":
    main()
