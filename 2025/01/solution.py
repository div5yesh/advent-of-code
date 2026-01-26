with open("sample.txt", "r") as file:
    content = file.read().split("\n")


def solution(content):
    result = 0
    start = 50
    for line in content:
        direction, distance = line[0], int(line[1:])

        if direction == "L":
            start = 100 + start - distance

        if direction == "R":
            start = start + distance

        start %= 100
        if start == 0:
            result += 1

    return result


def solution2(content):
    result = 0
    start = 50
    for line in content:
        direction, distance = line[0], int(line[1:])

        if direction == "L":
            start -= distance

        if direction == "R":
            start += distance

        if start <= 0:
            print(start)
            result += 1
            start = 100 + start
        elif start >= 100:
            print(start)
            result += 1

        start %= 100
        print(start, line)

    return result


print(solution(content))
print(solution2(content))
