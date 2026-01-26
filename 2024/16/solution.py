import heapq

with open('sample.txt', 'r') as file:
    content = file.read().split('\n')

def find_pos(grid, type):
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == type: return (i, j)

def solution(content):
    result = 0
    start_x, start_y = find_pos(content, "S")

    visited = set()
    queue = [(0, (start_x, start_y, ">"))]
    directions = {(-1,0): "^", (1,0): "v", (0,-1): "<", (0,1): ">"}
    while queue:
        cost, pos = heapq.heappop(queue)
        if content[pos[0]][pos[1]] == "E": return cost, pos
        for move, dir in directions.items():
            move_x, move_y = pos[0] + move[0], pos[1] + move[1]

            if (move_x, move_y, dir) in visited: continue

            if content[move_x][move_y] != "#":
                add_cost = 1000 if pos[2] != dir else 0
                heapq.heappush(queue, (cost + 1 + add_cost, (move_x, move_y, dir)))

        visited.add(pos)

    return result

class ListNode:
    def __init__(self, pos=None, dir=">", cost=0, parent=None):
        self.pos = pos
        self.dir = dir
        self.cost = cost
        self.parent = parent
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __str__(self):
        return str(self.pos) + "," + self.dir + ", " + str(self.cost) + "," + str(self.parent.pos if self.parent else "")
    

def solution2(content):
    result = 0
    start = find_pos(content, "S")
    end = None

    visited = set()
    queue = [(0, ListNode(start))]
    directions = {(-1,0): "^", (1,0): "v", (0,-1): "<", (0,1): ">"}
    while queue:
        cost, node = heapq.heappop(queue)
        # print(node)
        if content[node.pos[0]][node.pos[1]] == "E": 
            end = node
            break

        for move, dir in directions.items():
            move_x, move_y = node.pos[0] + move[0], node.pos[1] + move[1]

            if (move_x, move_y, dir) in visited: continue

            if content[move_x][move_y] != "#":
                total = cost + 1 + (1000 if node.dir != dir else 0)
                heapq.heappush(queue, (total, ListNode((move_x, move_y), dir, total, node)))

        visited.add((node.pos[0], node.pos[1], node.dir))

    curr = end
    while curr and curr.parent:
        print(curr.parent.pos)
        curr = curr.parent
        result += 1

    return result

print(solution(content)) # - 85440
print(solution2(content))