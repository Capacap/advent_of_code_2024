precomputed_mul = {}
precomputed_lhs = {}
precomputed_rhs = {}
precomputed_stones = {}

def split(parent):
    if parent == 0:
        return [1]
    
    if parent == 1:
        return [2024]
    
    if parent in precomputed_mul:
        return precomputed_mul[parent]

    if parent in precomputed_lhs:
        return [precomputed_lhs[parent], precomputed_rhs[rhs]]
    
    str_number = str(parent)
    str_length = len(str_number)
    if str_length % 2 == 0:
        mid = str_length // 2
        lhs = int(str_number[:mid])
        rhs = int(str_number[mid:])
        precomputed_lhs[parent] = lhs
        precomputed_rhs[parent] = rhs
        return [lhs, rhs]
    
    mul = parent * 2024
    precomputed_mul[parent] = mul
    return [mul]

def main() -> None:
    initial_stones = []
    with open("./day_11/input.txt", "r") as file:
        for substring in file.read().strip().split():
            initial_stones.append(int(substring))

    # stones = initial_stones.copy()
    # for i in range(25):
    #     print(i)
    #     for j in range(len(stones)):
    #         stones[j] = split(stones[j], stones)

    # print(len(stones)) # Part 1 - 203457

    # stones = initial_stones.copy()
    # for i in range(75):
    #     print(i)
    #     for j in range(len(stones)):
    #         stones[j] = split(stones[j], stones)

    total_stone_count = 0
    for stone in initial_stones:
        stone_count = 0
        total_children = []
        for _ in range(75):
            if stone in precomputed_stones:
                stone_count = precomputed_stones[stone]
                break

            children = split(stone)
            total_children.extend(children)
            total_child_count = len(total_children)
            precomputed_stones[stone] = total_child_count
            stone = children[0]
            stone_count = total_child_count
        total_stone_count += stone_count

    print(len(total_stone_count)) # Part 2

if __name__ == "__main__":
    main()
