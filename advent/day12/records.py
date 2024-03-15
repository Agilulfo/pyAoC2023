from functools import lru_cache


def fits_in(record, seq_len):
    left = record[:-seq_len]
    right = record[-seq_len:]
    return "#" not in left and "." not in right


def min_len(groups):
    return sum(groups) + len(groups) - 1


def count_fits(record, broken_sequence_len):
    first_broken = None
    last_broken = None
    gap_point = False

    for index, status in enumerate(record):
        match status:
            case ".":
                if first_broken is not None:
                    gap_point = True
            case "#":
                if first_broken is not None:
                    last_broken = index
                    if (
                        gap_point
                        or last_broken - first_broken + 1 > broken_sequence_len
                    ):
                        return 0

                else:
                    first_broken = index
                    last_broken = index

    search_area = None
    if first_broken is not None:
        search_area = record[
            max(0, last_broken - broken_sequence_len + 1) : first_broken
            + broken_sequence_len
        ]
    else:
        search_area = record

    contigious_counter = 0
    fits_counter = 0

    for index, status in enumerate(search_area):
        if status != ".":
            contigious_counter += 1
        else:
            contigious_counter = 0

        if contigious_counter >= broken_sequence_len:
            fits_counter += 1

    return fits_counter


@lru_cache(maxsize=10000)
def count_arrangements(record, groups):
    if len(groups) == 1:
        return count_fits(record, groups[0])

    first_group = groups[:1]
    remaining_groups = groups[1:]
    start = min_len(first_group)
    end = min_len(remaining_groups)

    break_point_combinations = []
    for break_point in range(start, len(record) - end):
        if record[break_point] != "#" and fits_in(record[:break_point], first_group[0]):
            break_point_combinations.append(
                count_arrangements(record[break_point + 1 :], remaining_groups)
            )

    return sum(break_point_combinations)
