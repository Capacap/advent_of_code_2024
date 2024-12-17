def find_first_free_block_index(blocks):
    for i in range(len(blocks)):
        if blocks[i] == -1:
            return i


def find_last_file_block_index(data):
    for i in range(len(data) - 1, 0, -1):
        if data[i] != -1:
            return i


def defrag(blocks):
    free_index = find_first_free_block_index(blocks)
    file_index = find_last_file_block_index(blocks)
    if free_index < file_index:
        blocks[free_index] = blocks[file_index]
        blocks[file_index] = -1
        return True
    return False


def main() -> None:
    blocks = []
    with open("./day_09/input.txt", "r") as file:
        text = file.read().strip()
        for i in range(0, len(text) - 1, 2):
            file_id = i // 2
            file_block_length = int(text[i])
            free_block_length = int(text[i + 1])
            blocks.extend([file_id] * file_block_length)
            blocks.extend([-1] * free_block_length)

    while True:
        success = defrag(blocks)
        if not success:
            break

    print(blocks[0:25])

    checksum = 0
    for i, id in enumerate(blocks):
        if id != -1:
            checksum += i * id
    print(checksum)

if __name__ == "__main__":
    main()
