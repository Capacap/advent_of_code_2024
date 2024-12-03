import re

def extract_multiplication_pairs(text: str):
    pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')
    matches = pattern.finditer(text)
    
    results = []
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        product = x * y
        pos = match.start()
        results.append((pos, product))
    
    return results

def extract_dos(text:str):
    pattern = re.compile(r'do\(\)')
    matches = pattern.finditer(text)
    
    results = []
    for match in matches:
        pos = match.start()
        results.append(pos)
    
    return results

def extract_donts(text:str):
    pattern = re.compile(r'don\'t\(\)')
    matches = pattern.finditer(text)
    
    results = []
    for match in matches:
        pos = match.start()
        results.append(pos)
    
    return results

def extract_do_and_dont_expressions(text:str):
    pattern = re.compile(r'do\(\)')
    matches = pattern.finditer(text)

    pattern = re.compile(r'don\'t\(\)')
    matches = pattern.finditer(text)
    
    results = []
    for match in matches:
        pos = match.start()
        results.append(pos)
    
    return results

def part_02() -> None:

    with open("./day_03/input.txt", 'r') as file:
        text = file.read()

    muls = extract_multiplication_pairs(text)
    dos = extract_dos(text)
    donts = extract_donts(text)

    #products = []
    #for product in muls
    #   pos = product[0]
    #   prod = product[1]
    #

    print(muls)
    print(dos)
    print(donts)


if __name__ == "__main__":
    part_02()