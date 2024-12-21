# import cProfile 
# import pstats 
# from pstats import SortKey
from functools import cache

@cache
def mutate(stone: int) -> tuple[int]:
    if stone == 0:
        return (1,)

    str_number: str = str(stone)
    str_length: int = len(str_number)
    if str_length % 2 == 0:
        mid: int = str_length // 2
        lhs: int = int(str_number[:mid])
        rhs: int = int(str_number[mid:])
        return (lhs, rhs)
    
    mul: int = stone * 2024
    return (mul,)

@cache
def count_final_mutations_recursive(stone: int, iterations: int) -> int:
    if iterations == 0:
        return 1
    
    final_mutations_count: int = 0
    for mutated in mutate(stone):
        final_mutations_count += count_final_mutations_recursive(mutated, iterations - 1)
    return final_mutations_count


def main() -> None:
    initial_stones = []
    with open("./day_11/input.txt", "r") as file:
        initial_stones = [int(substring) for substring in file.read().strip().split()]

    final_generation_stone_count = 0
    for init_stone in initial_stones:
        final_generation_stone_count += count_final_mutations_recursive(init_stone, 25)

    print(final_generation_stone_count) # Part 1 - 203457

    final_generation_stone_count = 0
    for init_stone in initial_stones:
        final_generation_stone_count += count_final_mutations_recursive(init_stone, 75)

    print(final_generation_stone_count) # Part 2 - 241394363462435


if __name__ == "__main__":
    #profiler = cProfile.Profile() 
    #profiler.enable() 
    main() 
    #profiler.disable() 
    #stats = pstats.Stats(profiler) 
    #stats.sort_stats(SortKey.TIME) 
    #stats.print_stats()