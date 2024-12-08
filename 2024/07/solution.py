with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def check(values, test):
    leaves = [values[0]]
    rest = values[1:]
    for value in rest:
        nodes = []
        for leaf in leaves:
            v1 = int(str(leaf) + str(value))
            if v1 <= test:
                nodes.append(v1)
            v2 = leaf + value
            if v2 <= test:
                nodes.append(v2)

            v3 = leaf * value
            if v3 <= test:
                nodes.append(v3)

        leaves = nodes

    return test in leaves

def solution(content):
    result = 0
    for line in content:
        test, values = line.split(": ")
        test = int(test)
        values = [int(x) for x in values.split(" ")]
        
        if check(values, test):
            result += test

    return result

print(solution(content))