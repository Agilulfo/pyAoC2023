from advent.day01 import shared

word_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    with open("./advent/day01/input") as input:
        calibration_value = 0
        for line in input:
            calibration_value += shared.extract_number(replace_number_words(line))
        print("the calibration_value is {0}".format(calibration_value))


def replace_number_words(line, cursor=0):
    if cursor == len(line):
        return line
    word = None
    for number in word_map.keys():
        if start_with(line[cursor:], number):
            word = number
            break

    if word:
        line = line.replace(word, word_map[word], 1)

    return replace_number_words(line, cursor=cursor + 1)


def start_with(line, word):
    line_len = len(line)
    word_len = len(word)
    if word_len > line_len:
        return False
    return line[:word_len] == word


if __name__ == "__main__":
    main()
