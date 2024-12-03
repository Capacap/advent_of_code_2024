import re

def extract_multiplication_pairs(text: str):
    pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')
    matches = pattern.findall(text)
    
    numbers = []
    for match in matches:
        x, y = map(int, match)
        numbers.append((x, y))

    return numbers


def part_01() -> None:

    with open("./day_03/input.txt", 'r') as file:
        text = file.read()

    multiplications = extract_multiplication_pairs(text)

    products = []
    for pair in multiplications:
        products.append(pair[0] * pair[1])

    print(sum(products))


if __name__ == "__main__":
    part_01()