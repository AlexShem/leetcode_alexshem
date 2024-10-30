from collections import defaultdict


def max_number_of_families(n: int, reserved_seats: list[list[int]]) -> int:
    reserved_seats.sort()
    reserved_by_row = defaultdict(list)
    for row, seat in reserved_seats:
        reserved_by_row[row].append(seat)

    result = 0
    for i in range(1, n + 1):
        if i not in reserved_by_row:
            result += 2
            continue

        reserved_in_row = reserved_by_row[i]

        # Try allocating two families
        if (len(reserved_in_row) <= 2
                and reserved_in_row[0] in [1, 10]
                and reserved_in_row[-1] in [1, 10]):
            result += 2
            continue

        # Try allocating one family
        possible_locations = [(2, 5), (4, 7), (6, 9)]
        for location in possible_locations:
            loc_possible = True
            for taken in reserved_in_row:
                if taken in range(location[0], location[1] + 1):
                    loc_possible = False
                    break
            if loc_possible:
                result += 1
                break
    return result
