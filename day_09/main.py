def main() -> None:
    with open("./day_09/input.txt", "r") as file:
        text = file.read().strip()
        for i in range(0, len(text), 2):
            file_id = i // 2
            file_blocks = int(text[i])
            free_blocks = int(text[i + 1])


if __name__ == "__main__":
    main()
