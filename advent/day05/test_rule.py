from advent.day05 import shared


def test_map():
    map = shared.Map("seed-to-soil", [[50, 98, 2], [52, 50, 48]])
    assert map.convert_id(50) == 52
    assert map.convert_id(97) == 99
    assert map.convert_id(98) == 50
    assert map.convert_id(100) == 100
    assert map.convert_id(49) == 49
