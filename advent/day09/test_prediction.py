from advent.day09.first import predict_next_value


def test_prediction():
    history = [0, 3, 6, 9, 12, 15]
    assert predict_next_value(history) == 18
