from advent.day09.prediction import predict_value


def test_prediction():
    history = [0, 3, 6, 9, 12, 15]
    assert predict_value(history) == 18


def test_prediction_backward():
    history = [10, 13, 16, 21, 30, 45]
    assert predict_value(history, forward=False) == 5
