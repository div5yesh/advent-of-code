with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def solution(content):
    antennas = {}
    for i, x in enumerate(content):
        for j, y in enumerate(x):
            if y != ".":
                if y not in antennas: antennas[y] = []
                antennas.get(y).append((i, j))

    antinodes = set()
    for value in antennas.values():
        print(value)
        for i in range(len(value)):
            for j in range(i, len(value)):
                p1, p2 = value[i], value[j]
                if i < j:
                    dx, dy = p1[0] - p2[0], p1[1] - p2[1]
                    if 0 <= p1[0]+dx < len(content) and 0 <= p1[1]+dy < len(content):
                        antinodes.add((p1[0]+dx, p1[1]+dy))
                    if 0 <= p2[0]-dx < len(content) and 0 <= p2[1]-dy < len(content):
                        antinodes.add((p2[0]-dx, p2[1]-dy))

    return len(antinodes)

print(solution(content)) # 275 - 395, 770