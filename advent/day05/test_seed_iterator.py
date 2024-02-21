from advent.day05 import second


def test_genrator():
    seed_iterator = second.SeedIterator([2, 2, 8, 3])
    seeds = [seed for seed in seed_iterator]
    assert seeds == [2, 3, 8, 9, 10]
