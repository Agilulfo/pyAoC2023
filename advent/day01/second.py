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
    "nine": "9"
}

def main ():
    with open("./advent/day01/input") as input :
        calibration_value = 0
        for line in input:
            calibration_value += shared.extract_number(replace_number_words(line))
        print("the calibration_value is {0}".format(calibration_value))

def replace_number_words(line):
    for k, v in word_map.items():
        line = line.replace(k, v)
    return line

if __name__ == "__main__" :
    main()
