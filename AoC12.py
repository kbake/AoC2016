# Advent of Code, D12_2016

INPUT = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 16 c
cpy 12 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

# INPUT = """cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a"""

def execute_instructions(instructions, registers):
    inc = lambda x: x + 1
    dec = lambda x: x - 1
    jnz = lambda x, y: y if x != 0 else 1
    functions = {"inc":inc, "dec":dec, "jnz":jnz}
    i = 0
    while i < len(instructions):
        instruction = instructions[i].split()
        if instruction[0] == "cpy":
            if instruction[1] in registers:
                registers[instruction[2]] = registers[instruction[1]]
            else:
                registers[instruction[2]] = int(instruction[1])
        elif instruction[0] == "jnz":
            if instruction[1] in registers:
                i += jnz(registers[instruction[1]], int(instruction[2]))
            else:
                i += jnz(int(instruction[1]), int(instruction[2]))
            continue
        else:
            func = functions[instruction[0]]
            registers[instruction[1]] = func(registers[instruction[1]])
        i += 1
    return registers

P1_START_REGISTERS = {"a":0, "b":0, "c":0, "d":0}
P2_START_REGISTERS = {"a":0, "b":0, "c":1, "d":0}
P1_RETURED = execute_instructions(INPUT.split('\n'), P1_START_REGISTERS)
P2_RETURNED = execute_instructions(INPUT.split('\n'), P2_START_REGISTERS)
print(P1_RETURED["a"])
print(P2_RETURNED["a"])
