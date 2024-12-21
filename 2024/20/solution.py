from collections import defaultdict
import heapq

with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def find_pos(grid, char):
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == char: return (i, j)

def viz(grid):
    for i, row in enumerate(grid):
        temp = ""
        for j, col in enumerate(row):
            temp += col
        print(temp)

def find_path(grid, start, end):
    length = len(grid)
    visited = set()
    que = [(0, start)]
    while que:
        cost, pos = heapq.heappop(que)
        if pos == end: return cost
        if pos in visited: continue

        for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
            move_x, move_y = pos[0] + dx, pos[1] + dy
            if 0 <= move_x < length and 0 <= move_y < length:
                if grid[move_x][move_y] != "#":
                    heapq.heappush(que, (cost + 1, (move_x, move_y)))

        visited.add(pos)

    print(start, end, "0 was here")
    return 0

def check_wall(grid, visited, start, wall):
    length = len(grid)
    wall_x, wall_y = wall
    for cx, cy in [[-1,0], [1,0], [0,-1], [0,1]]:
        cheat_x, cheat_y = wall_x + cx, wall_y + cy
        if (cheat_x, cheat_y) == start or (cheat_x, cheat_y) in visited: continue

        if 0 <= cheat_x < length and 0 <= cheat_y < length and content[cheat_x][cheat_y] != "#":
            saved = find_path(content, start, (cheat_x, cheat_y)) - 2
            return saved, (cheat_x, cheat_y)
        
    # print(start, wall, "invalid wall")
    return 0, None

def solution(content):
    result = 0
    start = find_pos(content, "S")
    end = find_pos(content, "E")

    length = len(content)
    visited = set()
    cheats = defaultdict(list)
    que = [(0, start)]
    while que:
        cost, pos = heapq.heappop(que)
        if pos == end:
            break

        if pos in visited: continue

        for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
            move_x, move_y = pos[0] + dx, pos[1] + dy
            if 0 <= move_x < length and 0 <= move_y < length:
                if content[move_x][move_y] == "#":
                    wall =  (move_x, move_y)
                    saved, cheat = check_wall(content, visited, pos, wall)
                    if cheat and saved > 0: cheats[saved] += [(wall, cheat)]
                else:
                    heapq.heappush(que, (cost + 1, (move_x, move_y)))

        visited.add(pos)
    
    ordered = sorted(cheats.keys())
    for key in ordered:
        if key >= 100: result += len(cheats[key])

    return result

def solution2(content):
    result = 0

    return result

print(solution(content))
print(solution2(content))