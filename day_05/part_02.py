import re
from typing import List, Dict


def validate_update(
    update: List[int],
    page_to_predecessors: Dict[int, List[int]],
    page_to_successors: Dict[int, List[int]],
) -> bool:
    for idx, page in enumerate(update):
        if idx != 0:
            predecessors = page_to_predecessors.get(page, [])
            for predecessor in predecessors:
                if predecessor in update and predecessor not in update[:idx]:
                    return False
        if idx != len(update) - 1:
            successors = page_to_successors.get(page, [])
            for successor in successors:
                if successor in update and successor not in update[idx + 1 :]:
                    return False
    return True


def part_02() -> None:
    with open("./day_05/input.txt", "r") as file:
        text = file.read()

    page_to_predecessors: Dict[int, List[int]] = {}
    page_to_successors: Dict[int, List[int]] = {}
    pair_pattern = re.compile(r"(\d+)\|(\d+)")
    for match in pair_pattern.finditer(text):
        if match.group(1) and match.group(2):
            lhs = int(match.group(1))
            rhs = int(match.group(2))
            if lhs in page_to_successors:
                page_to_successors[lhs].append(rhs)
            else:
                page_to_successors[lhs] = [rhs]
            if rhs in page_to_predecessors:
                page_to_predecessors[rhs].append(lhs)
            else:
                page_to_predecessors[rhs] = [lhs]

    updates: List[List[int]] = []
    comma_separated_pattern = re.compile(r"^\d+(,\d+)+$", re.MULTILINE)
    for match in comma_separated_pattern.finditer(text):
        line = match.group(0)
        num_list = list(map(int, line.split(",")))
        updates.append(num_list)

    invalid_updates: List[List[int]] = []
    for update in updates:
        if not validate_update(update, page_to_predecessors, page_to_successors):
            invalid_updates.append(update)

    for update in invalid_updates:
        while True:
            if validate_update(update, page_to_predecessors, page_to_successors):
                break
            for idx, page in enumerate(update):
                if idx != 0:
                    predecessors = page_to_predecessors.get(page, [])
                    for predecessor in predecessors:
                        if predecessor in update and predecessor not in update[:idx]:
                            pred_idx = update.index(predecessor)
                            pred_val = update.pop(pred_idx)
                            update.insert(idx - 1, pred_val)
                if idx != len(update) - 1:
                    successors = page_to_successors.get(page, [])
                    for successor in successors:
                        if successor in update and successor not in update[idx + 1 :]:
                            succ_idx = update.index(successor)
                            succ_val = update.pop(succ_idx)
                            update.insert(idx, succ_val)

    invalid_updates_middle_page: List[int] = []
    for update in invalid_updates:
        invalid_updates_middle_page.append(update[len(update) // 2])

    print(sum(invalid_updates_middle_page))


if __name__ == "__main__":
    part_02()
