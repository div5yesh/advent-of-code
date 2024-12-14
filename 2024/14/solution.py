import math

with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def viz(locations, r, c, fill=None):
    output = ""
    for i in range(r):
        temp = ""
        for j in range(c):
            if (i,j) in locations: temp += fill if fill else str(locations[(i,j)])
            else: temp += "."
        output += temp + "\n"
    return output

def solution(content):
    locations = {}
    rows, cols, time = 103, 101, 100
    quads = [0,0,0,0]
    mid = rows//2, cols//2
    for line in content:
        pos, vel = line.split(" ")
        pos = [int(x) for x in pos[2:].split(",")]
        vel = [int(x) for x in vel[2:].split(",")]

        new_y = (pos[0] + time * vel[0]) % cols
        new_x = (pos[1] + time * vel[1]) % rows
        locations[(new_x, new_y)] = locations.get((new_x, new_y), 0) + 1
        if new_x < mid[0] and new_y < mid[1]:
            quads[0] += 1
        elif new_x > mid[0] and new_y < mid[1]:
            quads[3] += 1
        elif new_x < mid[0] and new_y > mid[1]:
            quads[1] += 1
        elif new_x > mid[0] and new_y > mid[1]:
            quads[2] += 1

    return math.prod(quads)

def solution2(content):
    rows, cols = 103, 101
    with open('output.txt', 'w+') as file:
        for time in range(10_000):
            locations = {}
            for line in content:
                pos, vel = line.split(" ")
                pos = [int(x) for x in pos[2:].split(",")]
                vel = [int(x) for x in vel[2:].split(",")]

                new_y = (pos[0] + time * vel[0]) % cols
                new_x = (pos[1] + time * vel[1]) % rows
                locations[(new_x, new_y)] = locations.get((new_x, new_y), 0) + 1

            output = viz(locations, rows, cols, "1")
            if "1111111111111" in output:
                file.write(output + "\n\n" + str(time) + "\n")

print(solution(content))
print(solution2(content))