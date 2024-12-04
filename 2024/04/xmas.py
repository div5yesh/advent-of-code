with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def xmas(content):
    result = 0
    block = []
    for line in content:
        block += [line]

    lrow = len(block)
    lcol = len(block[0])

    for r in range(lrow):
        for c in range(lcol):
            if block[r][c] == "X":
                if c + 3 < lcol and block[r][c+1] == "M" and block[r][c+2] == "A" and block[r][c+3] == "S":
                    result += 1
                
                if c - 3 >= 0 and block[r][c-1] == "M" and block[r][c-2] == "A" and block[r][c-3] == "S":
                    result += 1

                if r + 3 < lrow and block[r+1][c] == "M" and block[r+2][c] == "A" and block[r+3][c] == "S":
                    result += 1
                
                if r - 3 >= 0 and block[r-1][c] == "M" and block[r-2][c] == "A" and block[r-3][c] == "S":
                    result += 1

                if r + 3 < lrow and c + 3 < lcol and block[r+1][c+1] == "M" and block[r+2][c+2] == "A" and block[r+3][c+3] == "S":
                    result += 1

                if r - 3 >= 0 and c - 3 >= 0 and block[r-1][c-1] == "M" and block[r-2][c-2] == "A" and block[r-3][c-3] == "S":
                    result += 1

                if r + 3 < lrow and c - 3 >= 0 and block[r+1][c-1] == "M" and block[r+2][c-2] == "A" and block[r+3][c-3] == "S":
                    result += 1

                if r - 3 >= 0 and c + 3 < lcol and block[r-1][c+1] == "M" and block[r-2][c+2] == "A" and block[r-3][c+3] == "S":
                    result += 1

    return result

def x_mas(content):
    result = 0
    lrow = len(content)
    lcol = len(content[0])

    groups = []
    for r in range(1, lrow - 1):
        for c in range(1, lcol -1 ):
            if content[r][c] == "A":
                groups += [content[r-1][c-1] + content[r][c] + content[r+1][c+1] + content[r-1][c+1] + content[r][c] + content[r+1][c-1]]
                
    for group in groups:
        result += group in ["MASMAS", "SAMSAM", "MASSAM", "SAMMAS"]
            
    return result

print(xmas(content)) # 2338 - 
print(x_mas(content)) # 190, 234 - 1517, 1784