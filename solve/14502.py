import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

result = 0

def get_safe_zone(data):
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                count += 1
    return count

def bfs(data):
    global result
    temp = [row[:] for row in data]
    q = deque()
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))
    while q:
        now = q.popleft()
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if temp[nr][nc] == 0:
                    temp[nr][nc] = 2
                    q.append((nr, nc))
    safe_zone = get_safe_zone(temp)
    result = max(result, safe_zone)

def dfs(depth):
    if depth == 3:
        bfs(data)
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                dfs(depth + 1)
                data[i][j] = 0

dfs(0)
print(result)
