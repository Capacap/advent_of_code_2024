from copy import copy
from typing import Dict, Tuple, Set
from itertools import product


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))


def main() -> None:
    test_values = []
    test_series = []
    with open("./day_07/input.txt", "r") as file:
        for line in file:
            series = list(map(int, line.strip().replace(":", "").split()))
            test_values.append(series[0])
            test_series.append(series[1:])

    test_validity = []
    for value, series in zip(test_values, test_series):
        for op_combo in set(product([add, mul], repeat=len(series) - 1)):
            valid = False

            lhs = series[0]
            for i, op in enumerate(op_combo):
                rhs = series[i + 1]
                lhs = op(lhs, rhs)
                if lhs > value:
                    break

            if lhs == value:
                valid = True
                break

        test_validity.append(valid)

    test_sum = sum([v for i, v in enumerate(test_values) if test_validity[i]])
    print(test_sum)  # Part 1 - 1708857123053

    test_validity = []
    for value, series in zip(test_values, test_series):
        valid = False
        for op_combo in set(product([add, mul, concat], repeat=len(series) - 1)):
            lhs = series[0]
            for i, op in enumerate(op_combo):
                rhs = series[i + 1]
                lhs = op(lhs, rhs)
                if lhs > value:
                    break

            if lhs == value:
                valid = True
                break

        test_validity.append(valid)

    test_sum = sum([v for i, v in enumerate(test_values) if test_validity[i]])
    print(test_sum)  # Part 2 - 189207836795655


if __name__ == "__main__":
    main()
