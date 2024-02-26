from advent.day09.parsing import parse_input
from advent.day09.prediction import predict_value


def main():
    oasis_report = parse_input()
    predictions = [predict_value(history, forward=False) for history in oasis_report]
    result = sum(predictions)
    print(f"The sum of all predictions is: {result}")
