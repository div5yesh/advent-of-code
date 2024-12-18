import heapq

with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def viz(grid):
    for i, row in enumerate(grid):
        temp = ""
        for j, col in enumerate(row):
            temp += col
        print(temp)

def find_path(grid):
    length = len(grid)
    visited = set()
    que = [(0,(0,0))]
    while que:
        cost, pos = heapq.heappop(que)
        if pos == (length - 1 ,length - 1): return cost
        if pos in visited: continue

        for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
            move_x, move_y = pos[0] + dx, pos[1] + dy
            if 0 <= move_x < length and 0 <= move_y < length:
                if grid[move_x][move_y] != "#":
                    heapq.heappush(que, (cost + 1, (move_x, move_y)))

        visited.add(pos)

    return None

def solution(content):
    bounds = 71
    bytes = 1024
    result = 0
    grid = [["." for i in range(bounds)] for i in range(bounds)]
    blocks = []
    for i, line in enumerate(content):
        if i == bytes: break
        coord = [int(x) for x in line.split(",")]
        blocks.append(coord)
        grid[coord[1]][coord[0]] = "#"

    result = find_path(grid)

    viz(grid)
    return result

def solution2(content):
    bounds = 71
    result = 0
    grid = [["." for i in range(bounds)] for i in range(bounds)]
    blocks = []
    for i, line in enumerate(content):
        coord = [int(x) for x in line.split(",")]
        blocks.append(coord)
        grid[coord[1]][coord[0]] = "#"

        if i < 1024 : continue
    
        block_x, block_y = coord
        result = find_path(grid)
        if not result: return (i, result, block_x, block_y)

    return result

print(solution(content))
print(solution2(content)) # (34, 43), (18, 37), (3,4), (4,3), (55, 32)