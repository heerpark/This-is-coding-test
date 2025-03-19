import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
data = []
drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

for _ in range(n):
    data.append(list(map(int, input().split())))

def bfs(row, col, group):
    q = deque()
    result = []
    q.append((row, col))
    while q:
        now = q.popleft()
        for i in range(4):
            nrow = now[0] + drow[i]
            ncol = now[1] + dcol[i]
            if 0 <= nrow < n and 0 <= ncol < n and group_table[nrow][ncol] == 0:
                if l <= abs(data[now[0]][now[1]] - data[nrow][ncol]) <= r:
                    q.append((nrow, ncol))
                    group_table[nrow][ncol] = group
                    result.append((nrow, ncol))
    return result

def merge(info):
    total = 0
    for row, col in info:
        total += data[row][col]
    avg = total // len(info)
    for row, col in info:
        data[row][col] = avg

day = 0

while True:
    group = 1
    group_table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if group_table[i][j] == 0:
                result = bfs(i, j, group)
                if len(result) > 0:
                    merge(result)
                    group += 1
    if group == 1:
        print(day)
        break
    day += 1

