import re

with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def mulling(content):
    result = 0
    operations = []
    for line in content:
        operations += re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)

    for operation in operations:
        trimmed = operation.replace("mul(", "").replace(")", "").split(",")
        result += (int(trimmed[0]) * int(trimmed[1]))

    return result

def filtered(content):
    result = 0
    operations = []
    for line in content:
        operations += re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line)

    enabled = True
    for operation in operations:
        if "mul" in operation and enabled:
            trimmed = operation.replace("mul(", "").replace(")", "").split(",")
            result += (int(trimmed[0]) * int(trimmed[1]))
        else:
            enabled = (operation == "do()")

    return result

print(mulling(content))
print(filtered(content)) # 21983, 2883946 - 173731097