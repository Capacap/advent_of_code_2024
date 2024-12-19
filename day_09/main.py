def find_first_free_block_index(blocks):
    for i, id in enumerate(blocks):
        if id == None:
            return i
        
def find_last_used_block_index(blocks):
    for i, id in enumerate(reversed(blocks)):
        if id != None:
            return (len(blocks) - 1) - i

def main() -> None:
    blocks = []
    with open("./day_09/input.txt", "r") as file:
        text = file.read()
        for i in range(0, len(text), 1):
            length = int(text[i])
            id = None if (i + 1) % 2 == 0 else i // 2
            blocks.extend([id] * length)

    #print(part_01(blocks)) # Part 1 - 6399153661894
    print(part_02(blocks)) # Part 2 - 9064931867050 too high
    #                                 10253030939061

def part_01(blocks):
    while True:
        free_index = find_first_free_block_index(blocks)
        used_index = find_last_used_block_index(blocks)
        if free_index > used_index:
            break
        blocks[free_index] = blocks[used_index]
        blocks[used_index] = None

    checksum = 0
    for i, id in enumerate(blocks):
        if id:
            checksum += id * i
    return checksum


def part_02(blocks):

    print(blocks[0:40]) 

    data_block_start_indices = []
    data_block_lengths = []

    free_block_start_indices = []
    free_block_lengths = []

    while True:

        data_block_start_indices.clear()
        data_block_lengths.clear()

        free_block_start_indices.clear()
        free_block_lengths.clear()

        prev_id = None
        for i, id in enumerate(blocks):

            if id == None and prev_id != None:
                free_block_start_indices.append(i)
                if len(data_block_start_indices) > 0:
                    data_block_lengths.append(i - data_block_start_indices[-1])

            if id != None and prev_id == None:
                data_block_start_indices.append(i)
                if len(free_block_start_indices) > 0:
                    free_block_lengths.append(i - free_block_start_indices[-1])

            if i == len(blocks) - 1:
                data_block_lengths.append(i - data_block_start_indices[-1])

            prev_id = id

        data_block_start_indices.reverse()
        data_block_lengths.reverse()

        def match_data_block_to_free_block():
            for i, data_block_length in enumerate(data_block_lengths):
                if data_block_length > 0:
                    for j, free_block_length in enumerate(free_block_lengths[0:len(data_block_lengths) - i]):
                        if free_block_length >= data_block_length:
                            print(f"MATCH {data_block_start_indices[i]} TO {free_block_start_indices[j]}")
                            return len(data_block_lengths) - i - 1, j
            return None, None

        data_block_index, free_block_index = match_data_block_to_free_block()

        if data_block_index == None or free_block_index == None:
            break

        data_block_start_index = data_block_start_indices[data_block_index]
        data_block_length = data_block_lengths[data_block_index]

        free_block_start_index = free_block_start_indices[free_block_index]
        free_block_length = free_block_lengths[free_block_index]

        for i in range(data_block_length):
            blocks[free_block_start_index + i] = blocks[data_block_start_index + i]
            blocks[data_block_start_index + i] = None

        free_block_start_indices[free_block_index] = free_block_start_index + data_block_length
        free_block_lengths[free_block_index] = free_block_length - data_block_length
        data_block_start_indices[data_block_index] = free_block_start_index

    print(blocks[0:40]) 

    checksum = 0
    for i, id in enumerate(blocks):
        if id:
            checksum += id * i
    return checksum

if __name__ == "__main__":
    main()
