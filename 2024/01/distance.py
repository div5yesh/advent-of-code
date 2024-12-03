import re

with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def find_distance(content):
    list1 = []
    list2 = []
    for line in content:
        pairs = line.split('   ')
        list1.append(int(pairs[0]))
        list2.append(int(pairs[1]))

    list1.sort()
    list2.sort()

    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
    
    return distance

def find_similarity(content):
    list1 = []
    map = {}
    for line in content:
        pairs = line.split('   ')
        list1.append(int(pairs[0]))
        map[int(pairs[1])] = map.get(int(pairs[1]), 0) + 1

    similarity = 0
    for i in range(len(list1)):
        similarity += list1[i] * map.get(list1[i] ,0)

    return similarity

print(find_distance(content))
print(find_similarity(content))