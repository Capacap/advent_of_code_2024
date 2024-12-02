from input import input


def main():
    left = input[::2]
    right = input[1::2]
    delta = []

    left.sort()
    right.sort()

    for x, y in zip(left, right):
        delta.append(abs(x - y))

    delta_sum = sum(delta)

    print(delta_sum)


if __name__ == "__main__":
    main()
