with open('input.txt', 'r') as file:
    content = file.read().split('\n\n')

def get_operand(registers, operand):
    if 0 <= operand <= 3: return operand
    if operand == 4: return registers[0]
    if operand == 5: return registers[1]
    if operand == 6: return registers[2]

def solution(content):
    result = []
    registers = []
    data = content[0].split("\n")
    for dt in data:
        registers += [int(dt[12:])]
    program = [int(x) for x in content[1][9:].split(",")]

    pointer = 0
    while pointer < len(program):
        inst = program[pointer]
        operand = program[pointer+1]

        if inst == 0:
            registers[0] = registers[0] // (2 ** get_operand(registers, operand))

        elif inst == 1:
            registers[1] = registers[1] ^ operand

        elif inst == 2:
            registers[1] = get_operand(registers, operand) % 8

        elif inst == 3:
            if registers[0] != 0:
                pointer = operand
                continue
            
        elif inst == 4:
            registers[1] = registers[1] ^ registers[2]
        
        elif inst == 5:
            result += [str(get_operand(registers, operand)%8)]

        elif inst == 6:
            registers[1] = registers[0] // (2 ** get_operand(registers, operand))

        elif inst == 7:
            registers[2] = registers[0] // (2 ** get_operand(registers, operand))
        
        pointer += 2

    return ",".join(result)

def solution2(content):
    result = 0

    return result

print(solution(content))
print(solution2(content))