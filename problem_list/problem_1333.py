def filter_restaurants(restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
    
    data_filtered = []
    for restaurant in restaurants:
        if veganFriendly == 1 and restaurant[2]:
            if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                data_filtered.append(restaurant)
        elif veganFriendly == 1 and not restaurant[2]:
            next
        elif veganFriendly == 0:
            if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                data_filtered.append(restaurant)
    
    data_sorted = sorted(data_filtered, key=lambda rest: (rest[1], rest[0]), reverse=True)
    # data_sorted.sort(key=lambda rest: rest[0])
    return [rest[0] for rest in data_sorted]


if __name__ == "__main__":
    # Test Case 1
    restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
    veganFriendly = 1
    maxPrice = 50
    maxDistance = 10
    expected_output = [3, 1, 5]
    result = filter_restaurants(restaurants, veganFriendly, maxPrice, maxDistance)
    print(f"Input: restaurants = {restaurants}, veganFriendly = {veganFriendly}, maxPrice = {maxPrice}, maxDistance = {maxDistance}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    print(f"Test Passed: {result == expected_output}\n")

    # Test Case 2
    restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
    veganFriendly = 0
    maxPrice = 50
    maxDistance = 10
    expected_output = [4, 3, 2, 1, 5]
    result = filter_restaurants(restaurants, veganFriendly, maxPrice, maxDistance)
    print(f"Input: restaurants = {restaurants}, veganFriendly = {veganFriendly}, maxPrice = {maxPrice}, maxDistance = {maxDistance}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    print(f"Test Passed: {result == expected_output}\n")

    # Test Case 3
    restaurants = restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
    veganFriendly = 0
    maxPrice = 30
    maxDistance = 3
    expected_output = [4, 5]
    result = filter_restaurants(restaurants, veganFriendly, maxPrice, maxDistance)
    print(f"Input: restaurants = {restaurants}, veganFriendly = {veganFriendly}, maxPrice = {maxPrice}, maxDistance = {maxDistance}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    print(f"Test Passed: {result == expected_output}\n")
    