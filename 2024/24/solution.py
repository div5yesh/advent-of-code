with open('input.txt', 'r') as file:
    content = file.read().split('\n\n')

def evaluate(operation, inputs, gates):
    if type(operation) is int: return operation

    if type(operation) is str: 
        return evaluate(inputs[operation] if operation in inputs else gates[operation], inputs, gates)

    if type(operation) is list:
        if operation[1] == "AND":
            return evaluate(operation[0], inputs, gates) & evaluate(operation[2], inputs, gates)
        if operation[1] == "OR":
            return evaluate(operation[0], inputs, gates) | evaluate(operation[2], inputs, gates)
        if operation[1] == "XOR":
            return evaluate(operation[0], inputs, gates) ^ evaluate(operation[2], inputs, gates)

def solution(content):
    result = 0
    wires = content[0].split("\n")
    connections = content[1].split("\n")

    inputs = {}
    for wire in wires:
        key, val = wire.split(":")
        inputs[key] = int(val)

    gates = {}
    for connection in connections:
        gate = connection.split(" ")
        gates[gate[4]] = gate[0:3]

    idx = 0
    binary = ""
    while True:
        key = "z" + (str(idx) if idx > 9 else "0" + str(idx))
        if key not in gates: break

        operation = gates[key]
        if type(operation) is list:
            binary = str(evaluate(operation, inputs, gates)) + binary

        idx += 1
    
    return binary, int(binary, 2)

def solution2(content):
    result = 0
    wires = content[0].split("\n")
    connections = content[1].split("\n")

    inputs = {}
    for wire in wires:
        key, val = wire.split(":")
        inputs[key] = int(val)

    gates = {}
    for connection in connections:
        gate = connection.split(" ")
        gates[gate[4]] = gate[0:3]

    idx = 0
    binary1 = ""
    binary2 = ""
    while True:
        key = "x" + (str(idx) if idx > 9 else "0" + str(idx))
        if key not in inputs: break
        binary1 = str(inputs[key]) + binary1

        key = "y" + (str(idx) if idx > 9 else "0" + str(idx))
        if key not in inputs: break
        binary2 = str(inputs[key]) + binary2

        idx += 1

    actual = solution(content)[0]
    expected = bin(int(binary1, 2) + int(binary2, 2))[2:]
    # print("0" + binary1)
    # print("0" + binary2)
    # print(expected)
    # print(actual)

    for i in range(len(expected)):
        value = actual[i] if i < len(actual) else 0
        if value != expected[i]:
            key = "z" + (str(i) if i > 9 else "0" + str(i))
            print(key, gates[gates[key][0]], gates[gates[key][2]], gates[key])

    return result

print(solution(content))
print(solution2(content))