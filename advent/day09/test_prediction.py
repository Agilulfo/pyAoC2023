from advent.day09.prediction import predict_value


def test_prediction():
    history = [0, 3, 6, 9, 12, 15]
    assert predict_value(history) == 18
