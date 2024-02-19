from advent.day03 import second


def test_extract_gears():
    map = [
        "..................",
        "....*.............",
        "..................",
        "..................",
        "...........*......",
        "..................",
        "..................",
        "..................",
        "*.................",
    ]
    assert second.extract_gears(map) == {
        (1, 4): [],
        (4, 11): [],
        (8, 0): [],
    }
