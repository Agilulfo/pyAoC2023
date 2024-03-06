import pytest
from advent.day12.records import ConditionRecord


def test_count_arrangements_full_match():
    r = ConditionRecord(".??.", [2])
    assert r.count_arrangements() == 1


def test_count_arrangements_complex():
    r = ConditionRecord("??.??.#??..#???#?#...", [3, 5, 1])
    assert r.count_arrangements() == 1


@pytest.mark.skip(reason="not yet implemented")
def test_count_arrangements_1():
    r = ConditionRecord(".???.", [2])
    assert r.count_arrangements() == 2


@pytest.mark.skip(reason="not yet implemented")
def test_count_arrangements_3():
    r = ConditionRecord(".?#?.", [2])
    assert r.count_arrangements() == 2


def test_count_arrangements_4():
    r = ConditionRecord("???#.", [2])
    assert r.count_arrangements() == 1


def test_fix_end_does_nothing():
    r = ConditionRecord("?????.??", [3])
    r.fix_end()
    assert r.damaged_record == "?????.??"
    assert r.verification_format == [3]


def test_fix_end_1():
    r = ConditionRecord("???#????#", [1, 3])
    r.fix_end()
    assert r.damaged_record == "???#?"
    assert r.verification_format == [1]


def test_fix_end_2():
    r = ConditionRecord("???#?.#??", [1, 3])
    r.fix_end()
    assert r.damaged_record == "???#?"
    assert r.verification_format == [1]


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


def test_remove_dots():
    r = ConditionRecord("....?????.....", [1])
    assert r.remove_dots()
    assert r.damaged_record == "?????"
