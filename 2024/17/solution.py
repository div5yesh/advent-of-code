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
    result = 0

    return result

print(solution(content))
print(solution2(content))