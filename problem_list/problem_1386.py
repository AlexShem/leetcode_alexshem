from collections import defaultdict


def max_number_of_families(n: int, reserved_seats: list[list[int]]) -> int:
    reserved_set = defaultdict(set)

    for row, seat in reserved_seats:
        if seat in {2, 3}:
            reserved_set[row].add(0)
        elif seat in {4, 5}:
            reserved_set[row].add(0)
            reserved_set[row].add(1)
        elif seat in {6, 7}:
            reserved_set[row].add(1)
            reserved_set[row].add(2)
        elif seat in {8, 9}:
            reserved_set[row].add(2)

    result = 2 * n
    for blocked in reserved_set.values():
        if len(blocked) == 3:
            result -= 2
        else:
            result -= 1

    return result
