def does_valid_array_exist(derived: list[int]) -> bool:
    val = derived[0]
    for i in range(1, len(derived)):
        val ^= derived[i]

    return val == 0
