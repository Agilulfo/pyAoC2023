from advent.day07 import first


def test_value():
    a = first.Hand("2AAAA", 1)
    b = first.Hand("44443", 2)
    assert a < b

    a = first.Hand("AAA45", 1)
    b = first.Hand("KKKKK", 2)
    assert a < b

    a = first.Hand("AAA22", 1)
    b = first.Hand("JJJJk", 2)
    assert a < b
