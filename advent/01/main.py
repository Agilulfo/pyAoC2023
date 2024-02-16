def main ():
    with open("./advent/01/input") as input :
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
    return join_digits(first, last)

def join_digits(first, last):
    if last:
        number = first + last
    else:
        number = first + first
    return int(number)


if __name__ == "__main__" :
    main()
