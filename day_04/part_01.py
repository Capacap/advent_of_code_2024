def part_01() -> None:
    lines = []
    with open("./day_04/input.txt", "r") as file:
        for line in file:
            lines.append(line.strip())

    width = len(lines[0])
    height = len(lines)
    count = 0

    # Horizontal check
    for y in range(height):
        for x in range(width - 3):
            letters = lines[y][x:x+4]
            if letters == "XMAS" or letters == "SAMX":
                count += 1

    # Vertical check
    for x in range(width):
        for y in range(height - 3):
            letters = "".join([lines[y+i][x] for i in range(4)])
            if letters == "XMAS" or letters == "SAMX":
                count += 1

    # Diagonal (top-left to bottom-right) check
    for y in range(height - 3):
        for x in range(width - 3):
            letters = "".join([lines[y+i][x+i] for i in range(4)])
            if letters == "XMAS" or letters == "SAMX":
                count += 1

    # Diagonal (bottom-left to top-right) check
    for y in range(3, height):
        for x in range(width - 3):
            letters = "".join([lines[y-i][x+i] for i in range(4)])
            if letters == "XMAS" or letters == "SAMX":
                count += 1

    print(count)

if __name__ == "__main__":
    part_01()
