import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, l, r = map(int, input().split())
data = []
drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

for _ in range(n):
    data.append(list(map(int, input().split())))


def merge(group):
    for i in range(1, group):
        total = 0
        position = []
        for row in range(n):
            for col in range(n):
                if group_table[row][col] == i:
                    total += data[row][col]
                    position.append((row, col))
        temp = total // len(position)
        for row, col in position:
            data[row][col] = temp



def dfs(i, j, group):
    flag = False
    for k in range(4):
        nr = i + drow[k]
        nc = j + dcol[k]
        if 0 <= nr < n and 0 <= nc < n and group_table[nr][nc] == 0:
            if l <= abs(data[i][j] - data[nr][nc]) <= r:
                group_table[i][j] = group
                group_table[nr][nc] = group
                dfs(nr, nc, group)
                flag = True
    return flag


day = 0
while True:
    group = 1
    group_table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(i, j, group) == True:
                group += 1

    if group == 1:
        print(day)
        break
    #국경이동계산
    merge(group)
    day += 1
