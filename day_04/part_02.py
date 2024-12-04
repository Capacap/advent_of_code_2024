def part_02() -> None:
    lines = []
    with open("./day_04/input.txt", "r") as file:
        for line in file:
            lines.append(line.strip())

    width = len(lines[0])
    height = len(lines)
    position_to_count = {}
    # Diagonal (top-left to bottom-right) check
    for y in range(height - 2):
        for x in range(width - 2):
            letters = "".join([lines[y + i][x + i] for i in range(3)])
            if letters == "MAS" or letters == "SAM":
                pos = (y + 1, x + 1)
                if pos in position_to_count:
                    position_to_count[pos] += 1
                else:
                    position_to_count[pos] = 1

    # Diagonal (bottom-left to top-right) check
    for y in range(2, height):
        for x in range(width - 2):
            letters = "".join([lines[y - i][x + i] for i in range(3)])
            if letters == "MAS" or letters == "SAM":
                pos = (y - 1, x + 1)
                if pos in position_to_count:
                    position_to_count[pos] += 1
                else:
                    position_to_count[pos] = 1

    duplicate_count = sum(1 for count in position_to_count.values() if count > 1)

    print(duplicate_count)

if __name__ == "__main__":
    part_02()
