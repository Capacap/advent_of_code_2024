precomputed_stones = {}

class Stone():
    __slots__ = ("number")

    def __init__(self, number):
        self.number: int = number

    def __repr__(self):
        return f"{self.number}"

    def split(self, collection):

        if self.number in precomputed_stones:
            stones = precomputed_stones[self.number]
            self.number = stones[0]
            collection.append(Stone(stones[1]))
            return

        if self.number == 0:
            self.number = 1
            return
        
        str_number = str(self.number)
        str_length = len(str_number)
        if str_length % 2 == 0:
            mid = str_length // 2
            lhs = int(str_number[:mid])
            rhs = int(str_number[mid:])
            precomputed_stones[self.number] = [lhs, rhs]
            self.number = lhs
            collection.append(Stone(rhs))
            return
        
        self.number = self.number * 2024

def main() -> None:
    initial_stones = []
    with open("./day_11/input.txt", "r") as file:
        for substring in file.read().strip().split():
            initial_stones.append(Stone(int(substring)))

    stones = initial_stones.copy()
    for i in range(25):
        print(i)
        for j in range(len(stones)):
            stones[j].split(stones)

    print(len(stones)) # Part 1 - 203457

    stones = initial_stones.copy()
    for i in range(75):
        print(i)
        for j in range(len(stones)):
            stones[j].split(stones)

    print(len(stones)) # Part 2

if __name__ == "__main__":
    main()
