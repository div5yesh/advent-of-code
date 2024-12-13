with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def solution(content):
    result = 0

    mapped = set()
    neighbors = {}
    areas = {}
    for i, line in enumerate(content):
        for j, cell in enumerate(line):
            if (i, j) in mapped: continue

            queue = [(i,j)]
            visited = set()
            while len(queue) > 0:
                topx, topy = queue.pop()
                neighbor = 0
                if (topx, topy) in visited: continue

                for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
                    x, y  = topx + dx, topy + dy
                    
                    if 0 <= x < len(content) and 0 <= y < len(content) and cell == content[x][y]:
                        neighbor += 1
                        if (x,y) not in visited:
                            queue.append((x,y))

                visited.add((topx, topy))
                neighbors[(i,j,cell)] = neighbors.get((i,j,cell), 0) + 4 - neighbor
                areas[(i,j,cell)] = areas.get((i,j,cell), 0) + 1

            mapped = mapped.union(visited)

    for plot, area in areas.items():
        result += area * neighbors[plot]
            
    return result


def solution2(content):
    result = 0

    return result

print(solution(content))
print(solution2(content))