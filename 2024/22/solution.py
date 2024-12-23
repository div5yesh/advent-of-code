from collections import defaultdict


with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def generate_old(secret):
    result = secret * 64
    secret = result ^ secret
    secret = secret % 16777216

    result = secret // 32
    secret = result ^ secret
    secret = secret % 16777216

    result = secret * 2048
    secret = result ^ secret
    secret = secret % 16777216
    return secret

def generate(secret):
    result = secret << 6
    secret = result ^ secret
    secret = secret % 16777216

    result = secret >> 5
    secret = result ^ secret
    secret = secret % 16777216

    result = secret << 11
    secret = result ^ secret
    secret = secret % 16777216 # (2 ^ 24)
    return secret

def solution(content):
    result = {}
    for secret in content:
        current = int(secret)
        for i in range(2000):
            current = generate(current)
        result[secret] = current

    return sum(result.values())

def solution2(content):
    # content = ['1','2','3','2024']
    result = defaultdict(list)
    changes = defaultdict(list)
    for secret in content:
        current = int(secret)
        for i in range(2000):
            ones = int(str(current)[-1])
            top = result[secret][-1] if result[secret] else ones
            change = ones - top
            result[secret] += [ones]
            changes[secret] += [change]
            current = generate(current)


    windows = {}
    for secret, prices in result.items():
        change = changes[secret]
        visited = set()
        for i in range(5, len(change)+1):
            seq = tuple(change[i-4:i])
            if seq not in visited:
                windows[seq] = windows.get(seq, 0) + prices[i-1]
                visited.add(seq)
    
    print(max(windows.values()))

print(solution(content))
print(solution2(content))