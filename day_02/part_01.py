from typing import List

def check_safe(series: List[int]) -> bool:
    desc = series[0] > series[-1]
    for curr, next in zip(series, series[1:]):
        if not (abs(next - curr) <= 3 and ((desc and next < curr) or (not desc and next > curr))):
            return False
    return True

def part_01() -> None:
    inputs = []
    with open("./day_02/input.txt", "r") as file:
        for line in file:
            series = list(map(int, line.strip().split()))
            inputs.append(series)

    unsafe_count = sum(not check_safe(series) for series in inputs)

    print(len(inputs) - unsafe_count)

if __name__ == "__main__":
    part_01()