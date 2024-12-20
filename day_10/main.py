def main() -> None:
    heightmap: dict[tuple, int]
    with open("./day_08/input.txt", "r") as file:
        for y, line in enumerate(file):
            max_y = max(max_y, y)
            for x, symbol in enumerate(line.strip()):
                max_x = max(max_x, x)
                height = int(symbol)

if __name__ == "__main__":
    main()
