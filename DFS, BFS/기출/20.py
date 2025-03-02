import sys

"""
point

백트래킹 + 감시하는거 구현
"""


input = sys.stdin.readline
n = int(input())
data = []
result = "NO"

def checker(row, col):
    for i in range(row-1, -1, -1):
        if data[i][col] == '0':
            break
        elif data[i][col] == 'S':
            return True
    for i in range(row, n):
        if data[i][col] == '0':
            break
        elif data[i][col] == 'S':
            return True
    for i in range(col-1, -1, -1):
        if data[row][i] == '0':
            break
        elif data[row][i] == 'S':
            return True
    for i in range(col, n):
        if data[row][i] == '0':
            break
        elif data[row][i] == 'S':
            return True
    return False


def gang():
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'T':
                if checker(i, j):
                    return True
    return False


for _ in range(n):
    data.append(list(input().split()))


def dfs(depth):
    global result
    if depth == 3:
        if result == "NO":
            if not gang():
                result = "YES"
        return
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = '0'
                dfs(depth + 1)
                data[i][j] = 'X'


dfs(0)
print(result)
