from  advent.day01 import shared

def main ():
    with open("./advent/day01/input") as input :
        calibration_value = 0
        for line in input:
            calibration_value += shared.extract_number(line)
        print("the calibration_value is {0}".format(calibration_value))

if __name__ == "__main__" :
    main()
