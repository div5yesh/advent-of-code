with open('sample1.txt', 'r') as file:
    content = file.read().split('\n\n')

def find_robot(grid):
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == "@": return (i, j)

def get_boxes(grid):
    boxes = set()
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == "O": boxes.add((i, j))

    return boxes

def transform(grid):
    scaled = []
    for i, line in enumerate(grid):
        scaled += [line.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")]

    return scaled

def viz(grid, robot, boxes=set()):
    for i, line in enumerate(grid):
        temp = ""
        for j, cell in enumerate(line):
            if cell == "#" or cell == "[" or cell == "]":
                temp += cell
            elif (i,j) in boxes:
                temp += "O"
            elif (i,j) == robot:
                temp += "@"
            else:
                temp += "."
        print(temp)

def solution(content):
    result = 0
    directions = {'^' : [-1,0], '>': [0,1], 'v': [1,0], '<': [0, -1]}
    grid = content[0].split("\n")
    movement = content[1].replace("\n", "")
    robot_x, robot_y = find_robot(grid)
    boxes = get_boxes(grid)
    
    for move in movement:
        dx, dy = directions[move]
        X, Y = (robot_x + dx, robot_y + dy)
        if grid[X][Y] == "#": continue

        moving = set()
        bx, by = X, Y
        while (bx, by) in boxes:
            moving.add((bx, by))
            bx += dx
            by += dy

        if grid[bx][by] == "#": 
            moving = set()
        else:
            robot_x, robot_y = X, Y

        boxes -= moving
        for box_x, box_y in moving:
            boxes.add((box_x + dx, box_y + dy))

    # viz(grid, (robot_x, robot_y), boxes)
    for box_x, box_y in boxes:
        result += (100 * box_x + box_y)

    return result

def solution2(content):
    result = 0
    directions = {'^' : [-1,0], '>': [0,1], 'v': [1,0], '<': [0, -1]}
    grid = content[0].split("\n")
    movement = content[1].replace("\n", "")

    grid = transform(grid)
    robot_x, robot_y = find_robot(grid)

    for move in movement:
        dx, dy = directions[move]
        X, Y = (robot_x + dx, robot_y + dy)
        if grid[X][Y] == "#": continue

        moving = set()
        if move == "<" or move == ">":
            bx, by = X, Y
            while True:
                if grid[bx][by] == "[":
                    moving.add((bx, by))
                    bx += 2 * dx
                    by += 2 * dy
                elif grid[bx][by] == "]":
                    moving.add((bx, by - 1))
                    bx += 2 * dx
                    by += 2 * dy
                else:
                    break

            if grid[bx][by] == "#": 
                moving = set()
            else:
                robot_x, robot_y = X, Y
            
            for x, y in moving:
                grid[x] = grid[x][:y-1] + "[]" + grid[x][y-1:]
                viz(grid, (robot_x, robot_y))
        
        print(moving)
        # boxes -= moving
        # for box_x, box_y in moving:
        #     boxes.add((box_x + dx, box_y + dy))


    # for box_x, box_y in boxes:
    #     result += (100 * box_x + box_y)
    
    return result

print(solution(content))
print(solution2(content))