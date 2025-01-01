class Potato():
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.instruction_ptr = 0
        self.output = []
        self._opcode_map = {
            0: self.adv, 
            1: self.bxl, 
            2: self.bst, 
            3: self.jnz, 
            4: self.bxc, 
            5: self.out, 
            6: self.bdv, 
            7: self.cdv,
        }

    def run(self):
        self.output.clear()
        self.instruction_ptr = 0
        while self.instruction_ptr < len(self.program):
            opcode = self.program[self.instruction_ptr]
            self._opcode_map[opcode]()

    def run_next(self):
        if self.instruction_ptr < len(self.program):
            opcode = self.program[self.instruction_ptr]
            self._opcode_map[opcode]()

            return True
        else:
            return False

    def debug_print(self):
        print(f"A: {self.a} - {bin(self.a)}")
        print(f"B: {self.b} - {bin(self.b)}")
        print(f"C: {self.c} - {bin(self.c)}")
        print(f"IP: {self.a}, OP: {self.operand()}, C_OP: {self.combo_operand()}")
        print(f"PROGRAM: {self.program}")
        print(f"OUTPUTS: {self.output}")

    def operand(self):
        if self.instruction_ptr + 1 >= len(self.program):
            return None

        return self.program[self.instruction_ptr + 1]

    def combo_operand(self):
        if self.instruction_ptr + 1 >= len(self.program):
            return None
        
        match self.operand():
            case 0 | 1 | 2 | 3: return self.operand()
            case 4: return self.a
            case 5: return self.b
            case 6: return self.c
            case 7: print("INVALID COMBO OPERAND")

    def adv(self):
        self.a = self.a // (2**self.combo_operand())
        self.instruction_ptr += 2

    def bdv(self):
        self.b = self.a // (2**self.combo_operand())
        self.instruction_ptr += 2

    def cdv(self):
        self.c = self.a // (2**self.combo_operand())
        self.instruction_ptr += 2

    def bxl(self):
        self.b = self.b ^ self.operand()
        self.instruction_ptr += 2

    def bxc(self):
        self.b = self.b ^ self.c
        self.instruction_ptr += 2

    def bst(self):
        self.b = self.combo_operand() % 8
        self.instruction_ptr += 2

    def jnz(self):
        if self.a == 0:
            self.instruction_ptr += 2
        else:
            self.instruction_ptr = self.operand()

    def out(self):
        self.output.append(self.combo_operand() % 8)
        self.instruction_ptr += 2

def parse_input(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()

    registers = {}
    for line in lines[:3]:
        name, value = line.strip().split(": ")
        registers[name] = int(value)

    program = list(map(int, lines[4].strip().split(": ")[1].split(",")))

    return (
        registers["Register A"],
        registers["Register B"],
        registers["Register C"],
        program,
    )

def main():
    a, b, c, program = parse_input("./day_17/input.txt")

    potato = Potato(a, b, c, program)
    potato.run()
    potato.debug_print()

if __name__ == "__main__":
    main()
