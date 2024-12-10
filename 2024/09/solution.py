with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def get_diskmap(content):
    diskmap = []
    id = 0
    for i in range(0, len(content)-1, 2):
        diskmap += [id] * int(content[i])
        diskmap += ["."] * int(content[i+1])
        id += 1

    diskmap += [id] * int(content[len(content) - 1])
    return diskmap

def get_checksum(diskmap):
    result = 0
    for i, x in enumerate(diskmap):
        if x != ".":
            result += i * int(x)

    return result

def solution(content):
    content = content[0]
    diskmap = get_diskmap(content)

    l, r = 0, len(diskmap) - 1
    while l < r:
        if diskmap[l] != ".":
            l += 1
        elif diskmap[r] == ".":
            r -= 1
        else:
            diskmap[l], diskmap[r] = diskmap[r], diskmap[l]

    return get_checksum(diskmap)

def solution2(content):
    content = content[0]
    diskmap = get_diskmap(content)

    highest = diskmap[-1]
    ptr = len(content) - 1
    rstart = len(diskmap) - 1
    for idx in range(highest, -1, -1):
        # find file
        while diskmap[rstart] != idx:
            rstart -= 1

        size = int(content[ptr])
        rend = rstart - size
        ptr -= 2

        lstart = 0
        while lstart < rend:
            # find empty
            if diskmap[lstart] == ".":
                # calculate space
                lend = lstart
                while diskmap[lend] == ".":
                    lend += 1

                space = lend - lstart

                if space >= size:
                    # copy
                    while rstart > rend:
                        diskmap[lstart], diskmap[rstart] = diskmap[rstart], diskmap[lstart]
                        lstart += 1
                        rstart -= 1
                    break

            lstart += 1

    return get_checksum(diskmap)

print(solution(content))
print(solution2(content)) # - 14331294549568, 15104730152444