from advent.day01 import second

def test_no_changes():
    assert second.replace_number_words("asd1dsad") == "asd1dsad"


def test_mixed_words():
    assert second.replace_number_words("eightwo2") == "8wo2"
