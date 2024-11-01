def find_kth_positive(arr: list[int], k: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        num = arr[mid]
        expected_index = num - 1
        actual_index = mid
        missing_count = expected_index - actual_index
        if missing_count < k:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1 + k


arr = [2, 3, 4, 7, 11]
k = 5
# Expected: 9
"""
left = 0
right = len(arr) ==> 5
mid = (left + right) // 2 ==> 2
arr[mid] ==> arr[2] ==> 4
If there were no missing numbers, the value 4 should have been on the position 3.
expected_index = arr[mid] - 1 ==> 3
actual_index = mid ==> 2
Since expected_index != actual_index, there are missing numbers before 4.
The number of missing numbers before is 4 is:
missing_count = expected_index - actual_index ==> 1
The number of missing numbers (1) is not equal k (5), so we continue the search.
"""

arr = [1, 2, 3, 4]
k = 2
# Expected: 6

arr = [2]
k = 1
# Expected: 1

arr = [3, 10]
k = 2
# Expected: 2

arr = [6, 7, 10, 20, 28, 29, 33, 37, 39, 40, 49, 53, 55, 72, 75, 76, 85, 87, 88, 94, 106, 107, 119, 120, 129, 142, 147,
       152, 157, 159, 161, 173, 178, 183, 187, 188, 193, 199, 202, 212, 215, 224, 227, 230, 237, 239, 246, 251, 256,
       260, 266, 268, 273, 277, 279, 281, 291, 297, 298, 310, 312, 314, 315, 321, 324, 326, 329, 341, 342, 348, 355,
       367, 370, 374, 387, 389, 394, 413, 420, 424, 429, 446, 447, 458, 460, 464, 467, 473, 477, 478, 498, 500, 501,
       503, 514, 515, 523, 525, 528, 529, 531, 535, 539, 555, 566, 569, 572, 583, 588, 591, 596, 602, 604, 605, 606,
       610, 611, 616, 619, 622, 623, 631, 632, 640, 642, 645, 647, 661, 680, 684, 685, 687, 694, 696, 698, 714, 717,
       720, 726, 734, 738, 742, 745, 753, 770, 775, 780, 781, 783, 787, 788, 798, 806, 821, 835, 852, 865, 873, 888,
       897, 926, 932, 935, 939, 945, 956, 966, 967, 969, 973, 979, 980, 986, 992, 995, 997]
k = 96
# Expected: 118

print(find_kth_positive(arr, k))
