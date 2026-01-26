import sys

sys.set_int_max_str_digits(50000)

with open('input.txt', 'r') as file:
    content = file.read().split('\n\n')

def get_operand(registers, operand):
    if 0 <= operand <= 3: return operand
    if operand == 4: return registers[0]
    if operand == 5: return registers[1]
    if operand == 6: return registers[2]

def solution(content, A=0):
    result = []
    registers = []
    data = content[0].split("\n")
    for dt in data:
        registers += [int(dt[12:])]
    program = [int(x) for x in content[1][9:].split(",")]

    registers[0] = A if A else registers[0]

    pointer = 0
    while pointer < len(program):
        inst = program[pointer]
        operand = program[pointer+1]

        if inst == 0:
            # A = A // 2 ** [0,1,2,3,A,B,C]
            registers[0] = registers[0] // (2 ** get_operand(registers, operand))

        elif inst == 1:
            # B = B ^ operand
            registers[1] = registers[1] ^ operand

        elif inst == 2:
            # B = [0,1,2,3,A,B,C] % 8
            registers[1] = get_operand(registers, operand) % 8

        elif inst == 3:
            if registers[0] != 0:
                pointer = operand
                continue
            
        elif inst == 4:
            # B = B ^ C
            registers[1] = registers[1] ^ registers[2]
        
        elif inst == 5:
            # out = [0,1,2,3,A,B,C] % 8
            result += [str(get_operand(registers, operand) % 8)]

        elif inst == 6:
            # B = A // 2 ** [0,1,2,3,A,B,C]
            registers[1] = registers[0] // (2 ** get_operand(registers, operand))

        elif inst == 7:
            # C = A // 2 ** [0,1,2,3,A,B,C]
            registers[2] = registers[0] // (2 ** get_operand(registers, operand))
        
        pointer += 2

    return ",".join(result)

def solution2(content):
    A = 0
    registers = []
    data = content[0].split("\n")
    for dt in data:
        registers += [int(dt[12:])]
    program = [int(x) for x in content[1][9:].split(",")]

    B = 0
    C = 0
    program.reverse()
    for inst in program:
        B = B + inst
        print("A: ", A)
        B = B ^ 6
        print("B: ", B)
        A *= 8
        print("A: ", A)
        B = B ^ C
        print("B: ", B)
        A = A * (2 ** B)
        # print("C: ", C)
        B = B ^ 5
        print("B: ", B)
        A = A + B
        print("C: ", C)

        # A = A + inst
        # A = A * 8

        # B = A % 8
        # B = B ^ 5
        # C = A // 2 ** B
        # B = B ^ C ^ 6
        # A = A // 8

        # out = B % 8
        # JMP 0

    return A

# print(solution(content))
print(solution2(content))

# 8x + r = 117440
# (117440/8)%8 = 0
# (14680/8)%8 = 3
# (1835/8)%8 = 5
# (229/8)%8 = 4
# (28/8)%8 = 3
# (3/8)%8 = 0

# ((((((((x + 0)8 + 3)8 + 4)8 + 5)8 + 3)8 + 0)8

# B = 200 % 8 = 0
# B = B ^ 5 = 0 ^ 5 = 5
# C = 200 // 2 ** 5(B) = 200//32 = 6
# B = B ^ C = 5 ^ 6 = 3
# A = 200 // 8 = 25
# B = B ^ 6 = 3 ^ 6 = 5
# out = B % 8 = 5 % 8 = 5

# out = 5 * 8 + 5
# B = 46
# A = 200 * 8 = 1600
# B = 46 ^ 6 = 40
# C = 1600 * 2 ** 40
# B = 40 ^ 5 = 40
# B = 1600 * 8