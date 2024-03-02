from advent.day12.records import ConditionRecord


def test_count_arrangements_full_match():
    r = ConditionRecord(".??.", [2])
    assert r.count_arrangements() == 1


def test_count_arrangements_complex():
    r = ConditionRecord("??.??.#??..#???#?#...", [3, 5, 1])
    assert r.count_arrangements() == 2


def test_count_arrangements_1():
    r = ConditionRecord(".???.", [2])
    assert r.count_arrangements() == 2


def test_count_arrangements_3():
    r = ConditionRecord(".?#?.", [2])
    assert r.count_arrangements() == 2


def test_count_arrangements_4():
    r = ConditionRecord("???#.", [2])
    assert r.count_arrangements() == 1


def test_chop_begin():
    r = ConditionRecord("?.#?#", [3])
    r.chop()
    assert r.damaged_record == "#?#"


def test_chop_end():
    r = ConditionRecord("#?#.??", [3])
    r.chop()
    assert r.damaged_record == "#?#"


def test_chop_end_short():
    r = ConditionRecord("#?#.?", [3])
    r.chop()
    assert r.damaged_record == "#?#"


def test_chop_no_changes():
    r = ConditionRecord("#?#", [3])
    r.chop()
    assert r.damaged_record == "#?#"


def test_chop_both_sides():
    r = ConditionRecord("??.??.#?#.??.??", [3])
    r.chop()
    assert r.damaged_record == "#?#"


def test_chop_complex():
    r = ConditionRecord("??.??.#??..#???#?#...", [3, 5, 1])
    r.chop()
    assert r.damaged_record == "#??..#???#?#"


def test_chop_complex_end():
    r = ConditionRecord("#??..#???#?#...", [3, 5, 1])
    r.chop()
    assert r.damaged_record == "#??..#???#?#"
