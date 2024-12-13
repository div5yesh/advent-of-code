with open('input.txt', 'r') as file:
    content = file.read().split('\n\n')

def solver(eq1, eq2):
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2

    B = (c2 * a1 - a2 * c1)/(b2 * a1 - b1 * a2)
    A = (c1 - b1 * B)/a1
    return A, B

def solution(content):
    result = 0
    for problem in content:
        conditions = problem.split("\n")
        cond_A = [int(param.strip()[2:]) for param in conditions[0][10:].split(",")]
        cond_B = [int(param.strip()[2:]) for param in conditions[1][10:].split(",")]
        cond_C = [int(param.strip()[2:]) for param in conditions[2][7:].split(",")]
        A, B = solver((cond_A[0], cond_B[0], cond_C[0]), (cond_A[1], cond_B[1], cond_C[1]))
        if A <= 100 and B <= 100 and A == int(A) and B == int(B):
            result += A * 3 + B 
    return int(result)

def solution2(content):
    result = 0
    for problem in content:
        conditions = problem.split("\n")
        cond_A = [int(param.strip()[2:]) for param in conditions[0][10:].split(",")]
        cond_B = [int(param.strip()[2:]) for param in conditions[1][10:].split(",")]
        cond_C = [int(param.strip()[2:]) for param in conditions[2][7:].split(",")]
        A, B = solver((cond_A[0], cond_B[0], 10_000_000_000_000 + cond_C[0]), (cond_A[1], cond_B[1], 10_000_000_000_000 + cond_C[1]))
        if A == int(A) and B == int(B):
            result += A * 3 + B 
    return int(result)

print(solution(content))
print(solution2(content))