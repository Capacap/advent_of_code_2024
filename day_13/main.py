import re


def parse_input(file_path: str) -> list[dict]:
    claw_machines = []
    pattern = re.compile(r"X[+=](\d+), Y[+=](\d+)")

    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")

        for i in range(0, len(lines), 4):
            a_match = pattern.search(lines[i])
            b_match = pattern.search(lines[i + 1])
            p_match = pattern.search(lines[i + 2])

            if a_match and b_match and p_match:
                a_x, a_y = map(int, a_match.groups())
                b_x, b_y = map(int, b_match.groups())
                p_x, p_y = map(int, p_match.groups())

                claw_machine = {"a": (a_x, a_y), "b": (b_x, b_y), "prize": (p_x, p_y)}

                claw_machines.append(claw_machine)

    return claw_machines


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def cramers_rule(a1, b1, c1, a2, b2, c2):
    # Create the coefficient matrix
    coeff_matrix = [[a1, b1], [a2, b2]]

    # Calculate the determinant of the coefficient matrix
    det = determinant(coeff_matrix)

    # Check if there is a unique solution
    if det == 0:
        return None

    # Create the matrices to find determinants for x and y
    matrix_x = [[c1, b1], [c2, b2]]
    matrix_y = [[a1, c1], [a2, c2]]

    # Calculate the determinants
    det_x = determinant(matrix_x)
    det_y = determinant(matrix_y)

    # Ensure the solutions are integers and not negative
    if det_x % det != 0 or det_y % det != 0 or det == 0:
        return None

    x = det_x // det
    y = det_y // det

    return int(x), int(y)


def calc_combo_cost(combo):
    i, j = combo
    return i * 3 + j * 1


def main() -> None:
    claw_machines = parse_input("./day_13/input.txt")

    total_cost = 0
    for claw_machine in claw_machines:
        ax, ay = claw_machine["a"]
        bx, by = claw_machine["b"]
        cx, cy = claw_machine["prize"]

        solution = cramers_rule(ax, bx, cx, ay, by, cy)

        if solution:
            total_cost += calc_combo_cost(solution)

    print(total_cost)  # Part 1 - 36954

    for claw_machine in claw_machines:
        xy = claw_machine["prize"]
        claw_machine["prize"] = (xy[0] + 10000000000000, xy[1] + 10000000000000)

    total_cost = 0
    for claw_machine in claw_machines:
        ax, ay = claw_machine["a"]
        bx, by = claw_machine["b"]
        cx, cy = claw_machine["prize"]

        solution = cramers_rule(ax, bx, cx, ay, by, cy)

        if solution:
            total_cost += calc_combo_cost(solution)

    print(total_cost)  # Part 2 - 79352015273424


if __name__ == "__main__":
    main()
