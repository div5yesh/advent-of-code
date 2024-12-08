with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def find_guard(content):
    for i, x in enumerate(content):
        for j, y in enumerate(x):
            if y == "^":
                return (i, j)

def solution(content):
    unsafe = set()
    length = len(content)
    guard = find_guard(content)
    unsafe.add(guard)

    current = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while 0 <= guard[0] < length and 0 <= guard[1] < length:
        [rdir, cdir] = directions[current % 4]
        if content[guard[0] + rdir][guard[1] + cdir] == "#":
            current += 1
        else:
            unsafe.add(guard)
            guard = (guard[0] + rdir, guard[1] + cdir)

    return len(unsafe)

print(solution(content))