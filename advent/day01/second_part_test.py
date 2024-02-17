from advent.day01 import second


def test_special_word():
    assert second.extract_number("2eightwo") == 22


def test_example():
    example = [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ]

    for word, number in example:
        assert second.extract_number(word) == number


def test_start_with():
    assert second.start_with("ciao", "ciao")
    assert second.start_with("ciaosss", "ciao")


def test_end_with():
    assert second.end_with("ciao", "ciao")
    assert second.end_with("ciaosss", "osss")
    assert not second.end_with("sss", "osss")


def test_first_number():
    assert second.find_first_number("xtwo3") == 2
