from advent.day05 import shared


def test_rule_lt():
    rule_a = shared.Rule((5, 7, 2))
    rule_b = shared.Rule((11, 34, 5))

    assert rule_a < rule_b
    assert rule_a < 9


def test_map():
    map = shared.Map("seed-to-soil", [[50, 98, 2], [52, 50, 48]])
    assert map.convert(50) == 52
    assert map.convert(97) == 99
    assert map.convert(98) == 50
    assert map.convert(100) == 100
    assert map.convert(49) == 49
