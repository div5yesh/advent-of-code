with open('input.txt', 'r') as file:
    content = file.read().split('\n\n')

def solution(content):
    result = 0
    patterns = set(content[0].replace(" ", "").split(","))
    designs = content[1].split("\n")

    for design in designs:
        found = [False] * (len(design) + 1)
        found[-1] = True
        for i in range(len(design), -1, -1):
            for pattern in patterns:
                if design[i:i+len(pattern)] == pattern:
                    found[i] = found[i+len(pattern)]
                if found[i]:
                    break

        if found[0]:
            result += 1
        
    return result

def solution2(content):
    result = 0
    patterns = set(content[0].replace(" ", "").split(","))
    designs = content[1].split("\n")

    for design in designs:
        found = [0] * (len(design) + 1)
        found[-1] = 1
        for i in range(len(design), -1, -1):
            for pattern in patterns:
                if design[i:i+len(pattern)] == pattern:
                    found[i] += found[i+len(pattern)]

        result += found[0]
        
    return result

print(solution(content))
print(solution2(content))