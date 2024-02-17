from advent.day01 import second
from advent.day01 import shared

def test_no_changes():
    assert second.replace_number_words("asd1dsad") == "asd1dsad"


def test_mixed_words():
    assert second.replace_number_words("eightwo2") == "8wo2"

def test_many_words():
    assert second.replace_number_words("ninenineightwo2two3tasdaone") == "99igh2223tasda1"

def test_example():
    example = [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76)
    ]

    for word, number in example:
        assert shared.extract_number(
            second.replace_number_words(
                word
            )
        ) == number

    assert False


def test_start_with():
    assert second.start_with("ciao", "ciao")
    assert second.start_with("ciaosss", "ciao")
