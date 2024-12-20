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
        return [precomputed_mul[parent]]

    if parent in precomputed_lhs:
        return [precomputed_lhs[parent], precomputed_rhs[parent]]
    
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

    total_stone_count = 0
    for initial_stone in initial_stones:
        if initial_stone in precomputed_stones:
            total_stone_count += precomputed_stones[initial_stone]
            continue

        stones = [initial_stone]
        final_child_count = 0
        for _ in range(75):
            print(_)
            
            children = []
            for i in range(len(stones)):
                children.extend(split(stones[i]))

            stones.clear()
            for child in children:
                if child in precomputed_stones:
                    total_stone_count += precomputed_stones[child]
                    continue
                stones.append(child)

        final_child_count = len(stones)
        total_stone_count += final_child_count
        precomputed_stones[initial_stone] = final_child_count


    print(total_stone_count) # Part 2

if __name__ == "__main__":
    main()
