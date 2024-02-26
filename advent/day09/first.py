from advent.day09.parsing import parse_input


def main():
    oasis_report = parse_input()
    predictions = [predict_next_value(history) for history in oasis_report]
    result = sum(predictions)
    print(f"The sum of all predictions is: {result}")


# example of analisys of a sensor reading history:

# 0   3   6   9  12  15
#   3   3   3   3   3
#     0   0   0   0

# at most we will need to produce other n - 1 lines
# for calulating the prediction value however we need to
# store only the last values
# don't think it is a too big of a deal so I'll initially
# simply implement the algorithm described in the challenge


def predict_next_value(history):
    delta_analisys = [history]

    for line in delta_analisys:
        if all_zeros(line):
            break
        next_line = [line[index + 1] - line[index] for index in range(len(line) - 1)]
        delta_analisys.append(next_line)

    next = 0
    for index in range(len(delta_analisys) - 2, -1, -1):
        next = delta_analisys[index][-1] + next

    return next


def all_zeros(values):
    for value in values:
        if value != 0:
            return False
    return True
