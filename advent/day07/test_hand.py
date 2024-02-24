from advent.day07.first import Scoring
from advent.day07.shared import Hand


def test_value():
    a = Hand("2AAAA", 1, Scoring)
    b = Hand("44443", 2, Scoring)
    assert a < b

    a = Hand("AAA45", 1, Scoring)
    b = Hand("KKKKK", 2, Scoring)
    assert a < b

    a = Hand("AAA22", 1, Scoring)
    b = Hand("JJJJ2", 2, Scoring)
    assert a < b
