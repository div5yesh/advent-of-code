import re

with open('input.txt', 'r') as file:
    content = file.read().split('\n')

def safe_reports(content):
    safe = 0
    for report in content:
        levels = [int(x) for x in report.split(" ")]
        increasing = True
        decreasing = True
        jump = True
        for i in range(1, len(levels)):
            increasing &= (levels[i-1] < levels[i])
            decreasing &= (levels[i-1] > levels[i])
            jump &= (abs(levels[i-1] - levels[i]) < 4)
        
        if (increasing or decreasing) and jump:
            safe += 1
    
    return safe

# [61, 64, 65, 66, 70, 73, 76] failed
def dampen(content):
    safe = 0
    for report in content:
        levels = [int(x) for x in report.split(" ")]
        increasing = 1
        decreasing = 1
        jump = 1
        length = len(levels)
        for i in range(1, length):
            if levels[i-1] < levels[i]: 
                increasing += 1 
            elif levels[i-1] > levels[i]:
                decreasing += 1

            if abs(levels[i-1] - levels[i]) < 4:
                jump += 1

        if ((increasing >= length - 1) or (decreasing >= length - 1)) and (jump == length):
            safe += 1
        elif ((increasing == length) or (decreasing == length)) and (jump >= length - 1):
            safe += 1

    return safe

def splitter(content):
    safe = 0
    for report in content:
        levels = [int(x) for x in report.split(" ")]
        is_safe = False
        for i in range(len(levels)):
            sub_levels = levels[:i] + levels[i+1:]
            increasing = True
            decreasing = True
            jump = True
            for i in range(1, len(sub_levels)):
                increasing &= (sub_levels[i-1] < sub_levels[i])
                decreasing &= (sub_levels[i-1] > sub_levels[i])
                jump &= (abs(sub_levels[i-1] - sub_levels[i]) < 4)
            
            is_safe |= ((increasing or decreasing) and jump)
        
        if is_safe: safe += 1
    
    return safe

print(safe_reports(content))
# print(dampen(content)) # 244 - 280
print(splitter(content))