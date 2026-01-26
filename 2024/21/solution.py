with open('sample.txt', 'r') as file:
    content = file.read().split('\n')

def solution(content):
    result = 0
    keypad = ["789", "456", "123", " 0A"]
    k_start = (3, 2)
    direction = [" ^A", "<v>"]
    d_start = (0, 2)
    coord = {}
    for i, row in enumerate(keypad):
        for j, col in enumerate(row):
            coord[col] = (i,j)

    coord_d = {}
    for i, row in enumerate(direction):
        for j, col in enumerate(row):
            coord_d[col] = (i,j)
    
    for code in content:
        pos = k_start
        seq1 = ""
        for ch in code:
            dx, dy = coord[ch][0] - pos[0], coord[ch][1] - pos[1]
            if dx < 0: seq1 += ("^" * abs(dx))
            elif dx > 0: seq1 += ("v" * dx)

            if dy < 0: seq1 += ("<" * abs(dy))
            elif dy > 0: seq1 += (">" * dy)

            seq1 += "A"
            pos = coord[ch]
        
        # seq1 = seq1.replace("^^<<", "<<^^")
        print(seq1)

        seq2 = ""
        pos = d_start
        for ch in seq1:
            dx, dy = coord_d[ch][0] - pos[0], coord_d[ch][1] - pos[1]
            if dx < 0: seq2 += ("^" * abs(dx))
            elif dx > 0: seq2 += ("v" * dx)

            if dy < 0: seq2 += ("<" * abs(dy))
            elif dy > 0: seq2 += (">" * dy)

            seq2 += "A"
            pos = coord_d[ch]

        print(seq2)

        seq3 = ""
        pos = d_start
        for ch in seq2:
            dx, dy = coord_d[ch][0] - pos[0], coord_d[ch][1] - pos[1]
            if dx < 0: seq3 += ("^" * abs(dx))
            elif dx > 0: seq3 += ("v" * dx)

            if dy < 0: seq3 += ("<" * abs(dy))
            elif dy > 0: seq3 += (">" * dy)

            seq3 += "A"
            pos = coord_d[ch]

        print(seq3, len(seq3), int(code[:3]))

        result += (len(seq3) * int(code[:3]))

    return result

def solution2(content):
    result = 0

    return result

print(solution(content)) # - 281984, 284004
print(solution2(content))

# v<<A^>>AvA^A v<<A^>>AAv<A<A^>>AA<Av>AA^Av<A^>AA<A>Av<A<A^>>AAA<Av>A^A
# <v<A>>^AvA^A <vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AA    AvA<^A>A

# <A>A v<<AA>^AA> AvAA^A<vAAA>^A
# <A>A <AAv<AA^>> AvAA^Av<AAA^>A

# ^A^^<<A>>AvvvA
# ^A<<^^A>>AvvvA