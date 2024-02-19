from advent.day03 import first

def test_extract_multiple_numbers():
    map = ["...2312..32.."]
    numbers = first.extract_numbers(map)
    assert numbers == [
        (2312, 0, 3,6),
        (32, 0, 9, 10)
    ]

def test_extract_multiple_numbers_limits():
    map = ["2312.......32"]
    numbers = first.extract_numbers(map)
    assert numbers == [
        (2312, 0, 0,3),
        (32, 0, 13, 14)
    ]

def test_extract_multiple_numbers_limitss():
    map = [
        "2312.......32",
        "............2",
        "..........2.3",
    ]
    numbers = first.extract_numbers(map)
    assert numbers == [
        (2312, 0, 0,3),
        (32, 0, 13, 14)
    ]
