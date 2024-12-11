with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def split(num):
    if num == "0":
        return ["1"]
    
    length = len(num)
    if length % 2 == 0:
        mid = length//2
        left = str(int(num[:mid]))
        right = str(int(num[mid:]))
        return [left, right]
    
    return [str(int(num) * 2024)]

def solution(content):
    stones = content[0].split(" ")

    for i in range(25):
        result = []
        for stone in stones:
            result += split(stone)
        stones = result
    
    return len(stones)

def solution2(content):
    stones = content[0].split(" ")

    stones = { k: 1 for k in stones }
    for i in range(75):
        result = {}
        for stone, count in stones.items():
            new_stones = split(stone)
            for new_stone in new_stones:
                result[new_stone] = result.get(new_stone, 0) + count
        stones = result
    
    return sum(result.values())

print(solution(content))
print(solution2(content))