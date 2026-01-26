with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def find_guard(content):
    for i, x in enumerate(content):
        for j, y in enumerate(x):
            if y == "^":
                return (i, j)

def find_loop(content, obstacle):
    length = len(content)
    guard = find_guard(content)
    guard2 = (guard[0], guard[1])

    current = 0
    current2 = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while True:
        [rdir, cdir] = directions[current2 % 4]
        if not (0 <= guard2[0] + rdir < length and 0 <= guard2[1] + cdir < length): return False

        if content[guard2[0] + rdir][guard2[1] + cdir] == "#" or (guard2[0] + rdir, guard2[1] + cdir) == obstacle:
            current2 += 1
        else:
            guard2 = (guard2[0] + rdir, guard2[1] + cdir)

        [rdir, cdir] = directions[current2 % 4]
        if not (0 <= guard2[0] + rdir < length and 0 <= guard2[1] + cdir < length): return False

        if content[guard2[0] + rdir][guard2[1] + cdir] == "#" or (guard2[0] + rdir, guard2[1] + cdir) == obstacle:
            current2 += 1
        else:
            guard2 = (guard2[0] + rdir, guard2[1] + cdir)

        [rdir, cdir] = directions[current % 4]
        if content[guard[0] + rdir][guard[1] + cdir] == "#" or (guard[0] + rdir, guard[1] + cdir) == obstacle:
            current += 1
        else:
            guard = (guard[0] + rdir, guard[1] + cdir)
        
        if guard == guard2:
            return True
    
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

def solution2(content):
    unsafe = set()
    length = len(content)
    guard = find_guard(content)
    result = 0

    current = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while 0 <= guard[0] < length and 0 <= guard[1] < length:
        [rdir, cdir] = directions[current % 4]
        if content[guard[0] + rdir][guard[1] + cdir] == "#":
            current += 1
        else:
            unsafe.add(guard)
            guard = (guard[0] + rdir, guard[1] + cdir)

    for obstacle in unsafe:
        if find_loop(content, obstacle):
            result += 1

    return result

print(solution(content))
print(solution2(content)) # - 1563