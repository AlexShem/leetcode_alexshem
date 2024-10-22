from tests.test_2659_count_operations_to_empty_array import test, NUMBER_OF_TESTS


def run_all_tests():
    all_tests_pass = True
    for test_no in range(1, NUMBER_OF_TESTS + 1):
        try:
            if not test(test_no):
                print(f"Test {test_no} failed")
                all_tests_pass = False
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    if all_tests_pass:
        print("All tests pass")
    else:
        print("Some tests failed")


if __name__ == "__main__":
    run_all_tests()
