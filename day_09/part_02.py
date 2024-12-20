class FileBlock:
    def __init__(self, id, location, size):
        self.id: int = id
        self.location: int = location
        self.size: int = size

    def __str__(self) -> str:
        return f"(ID: {self.id}, LOC: {self.location}, SIZE: {self.size})"

    def __repr__(self) -> str:
        return f"(ID: {self.id}, LOC: {self.location}, SIZE: {self.size})"

    def calc_checksum(self) -> int:
        if self.id == None:
            return 0

        checksum = 0
        for i in range(self.size):
            checksum += (self.location + i) * self.id
        return checksum


def find_next_file_block_index(file_blocks: list[FileBlock], forbidden: set[FileBlock]) -> int:
    for i, fb in enumerate(reversed(file_blocks)):
        if fb.id != None and fb.id not in forbidden:
            return len(file_blocks) - i - 1
    return -1


def main() -> None:
    file_blocks: list[FileBlock] = []
    with open("./day_09/input.txt", "r") as file:
        text = file.read()
        current_location = 0
        for i in range(0, len(text), 1):
            size = int(text[i])
            if size > 0:
                id = i // 2 if not (i + 1) % 2 == 0 else None
                file_block = FileBlock(id, current_location, size)
                file_blocks.append(file_block)
            current_location += size

    forbidden: set[int] = set()

    while True:
        fb_index = find_next_file_block_index(file_blocks, forbidden)
        if fb_index == -1:
            break

        forbidden.add(file_blocks[fb_index].id)

        for i in range(fb_index):
            if file_blocks[i].id != None:
                continue
            
            if file_blocks[i].size >= file_blocks[fb_index].size:
                file_blocks[fb_index].location = file_blocks[i].location
                file_blocks[i].size -= file_blocks[fb_index].size
                file_blocks[i].location += file_blocks[fb_index].size
                break

    checksum = 0
    for fb in file_blocks:
        checksum += fb.calc_checksum()
    print(checksum) # Part 2 - 6421724645083


if __name__ == "__main__":
    main()
