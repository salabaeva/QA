def sum(param):
    pass
    sum_result = 5
    # param[1] + param[2] + param[3]
    return sum_result


def test_sum():
    print("Validation")
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    print("Start test")
    test_sum()
    print("Everything passed")

if __name__ == "__main__":
    print("Start test2")
test_sum()
print("Everything passed")

