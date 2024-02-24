from advent.day07.scoring import Scoring
from advent.day07.shared import Hand
from advent.day07.first import card_value_mapping


def test_value():
    a = Hand("2AAAA", 1, Scoring(card_value_mapping))
    b = Hand("44443", 2, Scoring(card_value_mapping))
    assert a < b

    a = Hand("AAA45", 1, Scoring(card_value_mapping))
    b = Hand("KKKKK", 2, Scoring(card_value_mapping))
    assert a < b

    a = Hand("AAA22", 1, Scoring(card_value_mapping))
    b = Hand("JJJJ2", 2, Scoring(card_value_mapping))
    assert a < b
