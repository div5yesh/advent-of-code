with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def solution(content):
    result = 0
    heads = []
    for i, x in enumerate(content):
        for j, y in enumerate(x):
            if y == "0":
                heads += [[i, j, int(y)]]

    for head in heads:
        queue = [head]
        score = 0
        visited = set()
        while len(queue) > 0:
            next = queue.pop()
            for dir in [[-1,0], [1,0], [0,-1], [0,1]]:
                x_next, y_next, step = next[0] + dir[0], next[1] + dir[1], next[2]
                
                if 0 <= x_next < len(content) and 0 <= y_next < len(content):
                    if step == 9:
                        score += 1
                        break

                    if step + 1 == int(content[x_next][y_next]) and (x_next, y_next) not in visited:
                        visited.add((x_next, y_next))
                        queue.append((x_next, y_next, step+1))
        result += score

    return result

def solution2(content):
    result = 0
    heads = []
    for i, x in enumerate(content):
        for j, y in enumerate(x):
            if y == "0":
                heads += [[i, j, int(y)]]

    for head in heads:
        queue = [head]
        rating = 0
        while len(queue) > 0:
            next = queue.pop()
            for dir in [[-1,0], [1,0], [0,-1], [0,1]]:
                x_next, y_next, step = next[0] + dir[0], next[1] + dir[1], next[2]
                
                if 0 <= x_next < len(content) and 0 <= y_next < len(content):
                    if step == 9:
                        rating += 1
                        break

                    if step + 1 == int(content[x_next][y_next]):
                        queue.append((x_next, y_next, step+1))
        result += rating

    return result

print(solution(content))
print(solution2(content))