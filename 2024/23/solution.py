from collections import defaultdict
import heapq

with open('sample.txt', 'r') as file:
    content = file.read().split('\n')

def solution(content):
    result = 0
    adj = defaultdict(list)
    for connection in content:
        a, b = connection.split("-")
        adj[a] += [b]
        adj[b] += [a]

    for node in adj.keys():
        if "co" not in node: continue
        visited = set()
        print(node)

        que = [(0, node)]
        while que:
            depth, curr = heapq.heappop(que)

            print(que)
            if curr == node and depth == 3:
                result += 1
                # break


            if depth < 3:
                for edge in adj[curr]:
                    if edge in visited: continue
                    heapq.heappush(que, (depth + 1, edge))
            
            visited.add(curr)

    return result

def solution2(content):
    result = 0

    return result

print(solution(content))
print(solution2(content))