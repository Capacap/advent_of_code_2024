import re


def parse_text_for_valid_muls(text):
    pattern = re.compile(
        r"""
        mul\((\d+),\s*(\d+)\)     # Match mul(x, y) with x and y as numbers
        |                         # OR
        do\(\)                    # Match do()
        |                         # OR
        don\'t\(\)                # Match don't()
        """,
        re.VERBOSE,
    )
    matches = pattern.finditer(text)

    results = []
    do_muls = True
    for match in matches:
        if match.group(1) and match.group(2):
            if do_muls:
                x = int(match.group(1))
                y = int(match.group(2))
                results.append(x * y)
        elif match.group(0) == "do()":
            do_muls = True
        elif match.group(0) == "don't()":
            do_muls = False

    return results


def part_02() -> None:
    with open("./day_03/input.txt", "r") as file:
        text = file.read()

    results = parse_text_for_valid_muls(text)

    print(sum(results))


if __name__ == "__main__":
    part_02()
