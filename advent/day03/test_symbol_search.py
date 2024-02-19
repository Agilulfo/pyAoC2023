from advent.day03 import first

def test_find_symbol():
    assert    first.submap_has_symbol(
        [
         "....",
         ".12.",
         "..#."
        ]
    )

    assert   not  first.submap_has_symbol(
        [
         "....",
         ".12.",
         "...."
        ]
    )
