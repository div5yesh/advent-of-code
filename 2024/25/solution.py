with open('sample.txt', 'r') as file:
    content = file.read().split('\n\n')

def viz(grid):
    for i, row in enumerate(grid):
        temp = ""
        for j, cell in enumerate(row):
            temp += cell
        print(temp)
    print("\n")

def solution(content):
    result = 0
    locks, keys = [], []
    for schema in content:
        schema = schema.split("\n")
        if schema[0][0] == "#": locks += [schema]
        if schema[0][0] == ".": keys += [schema]

    lheight, kheight = [], []
    for lock in locks:
        heights = [0] * len(lock[0])
        for i in range(1, len(lock)):
            row = lock[i]
            for j, col in enumerate(row):
                if col == "#": heights[j] += 1
        lheight += [heights]

    for key in keys:
        heights = [0] * len(key[0])
        for i in range(len(key)-1):
            row = key[i]
            for j, col in enumerate(row):
                if col == "#": heights[j] += 1
        kheight += [heights]

    for lh in lheight:
        for kh in kheight:
            valid = True
            for i in range(len(lh)):
                valid &= (lh[i] + kh[i] <= 5)
            
            if valid: result += 1

    return result

def solution2(content):
    result = 0

    return result

print(solution(content))
print(solution2(content))