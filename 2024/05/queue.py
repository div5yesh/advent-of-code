with open('input.txt', 'r') as file:
    content = file.read().split('\n\n')

def update(content):
    result = 0
    rulemap = {}
    rules = content[0].split("\n")
    pages = content[1].split("\n")

    for rule in rules:
        order = rule.split("|")
        if order[0] not in rulemap: rulemap[order[0]] = set()
        rulemap[order[0]].add(order[1])

    for page in pages:
        items = page.split(",")
        valid = True
        length = len(items)
        for i in range(length - 1):
            for j in range(i + 1, length):
                valid &= (items[i] in rulemap and items[j] in rulemap[items[i]])
        
        if valid: result += int(items[length//2])

    return result

def fixed(content):
    result = 0
    rulemap = {}
    rules = content[0].split("\n")
    pages = content[1].split("\n")

    for rule in rules:
        order = rule.split("|")
        if order[0] not in rulemap: rulemap[order[0]] = set()
        rulemap[order[0]].add(order[1])

    rest = []
    for page in pages:
        items = page.split(",")
        valid = True
        length = len(items)
        for i in range(length - 1):
            for j in range(i + 1, length):
                valid &= (items[i] in rulemap and items[j] in rulemap[items[i]])

        if not valid: rest += [items]

    for items in rest:
        print(items)
        length = len(items)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if items[i] in rulemap and items[j] not in rulemap[items[i]]:
                    items[i], items[j] = items[j], items[i]

        result += int(items[length//2])

    return result

print(update(content))
print(fixed(content)) # 4998 - 