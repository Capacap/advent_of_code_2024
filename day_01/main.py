from input import input


def part_01():
    left = input[::2]
    right = input[1::2]
    delta = []

    left.sort()
    right.sort()

    for x, y in zip(left, right):
        delta.append(abs(x - y))

    delta_sum = sum(delta)

    print(delta_sum)


def part_02():
    left = input[::2]
    right = input[1::2]

    number_to_count = {}
    for number in left:
        count = 0
        for other_number in right:
            if number == other_number:
                count += 1
        number_to_count[number] = count

    similarity = []
    for number in left:
        try:
            count = number_to_count[number]
        except:
            count = 0
        similarity.append(number * count)

    score = sum(similarity)

    print(score)


if __name__ == "__main__":
    part_01()
    part_02()
