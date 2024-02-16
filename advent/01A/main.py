import os

def main ():
    print(os.getcwd())
    with open("./advent/01A/input") as input :
        calibration_value = 0
        for line in input:
            calibration_value += extract_number(line)
        print("the calibration_value is {0}".format(calibration_value))


def extract_number(line):
    first = None
    last  = None
    print(line)
    for char in line:
        if str.isdigit(char):
            if first :
                last = char
            else :
                first = char
    print("f: {}, l:{}".format(first, last))

    return join_digits(first, last)

def join_digits(first, last):
    if last:
        number = first + last
    else:
        number = first + first

    print(number)
    return int(number)


if __name__ == "__main__" :
    main()
