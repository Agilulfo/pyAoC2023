from advent.day03 import first


def test_extract_multiple_numbers():
    map = ["...2312..32.."]
    numbers = first.extract_numbers(map)
    assert numbers == [(2312, 0, 3, 6), (32, 0, 9, 10)]


def test_extract_numbers_close_to_borders():
    map = ["2312.......32"]
    numbers = first.extract_numbers(map)
    assert numbers == [(2312, 0, 0, 3), (32, 0, 11, 12)]


def test_extract_multiplae_numbers_limitss():
    map = [
        "32..50......",
        "............2",
        "..........2.3",
    ]
    numbers = first.extract_numbers(map)
    assert numbers == [
        (32, 0, 0, 1),
        (50, 0, 4, 5),
        (2, 1, 12, 12),
        (2, 2, 10, 10),
        (3, 2, 12, 12),
    ]
