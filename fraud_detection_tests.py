import fraud_detection as fd
import math


def test_ones_and_tens_digit_histogram():
    # example from spec
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])


def test_ones_and_tens_digit_histo_again():
    actual = fd.ones_and_tens_digit_histogram([0, 1, 1, 2, 3, 5, 8, 13,
                                               21, 34, 55, 89, 144, 233,
                                               377, 610, 987, 1597, 2584,
                                               4181, 6765])
    expected = [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,
                0.11904761904761904, 0.09523809523809523, 0.09523809523809523,
                0.023809523809523808, 0.09523809523809523, 0.11904761904761904,
                0.047619047619047616]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])


def test_mean_squared_error():
    actual = fd.mean_squared_error([1, 4, 9], [6, 5, 4])
    expected = 17.0
    assert actual == expected


def test_random_int_list():
    lst = fd.random_int_list(456)
    assert len(lst) == 456
    for x in lst:
        assert x < 100
        assert x >= 0


def main():
    test_ones_and_tens_digit_histogram()
    # call other test functions here


if __name__ == "__main__":
    main()
