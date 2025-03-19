import sys
import copy
from collections import deque

input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))


def bfs(visited, r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        nr, nc = q.popleft()
        for i in range(4):
            tr = nr + dr[i]
            tc = nc + dc[i]
            if 0 <= tr < n and 0 <= tc < m:
                if not visited[tr][tc] and data[tr][tc] != 0:
                    visited[tr][tc] = True
                    q.append((tr, tc))


def is_all_melt():
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0:
                return False
    return True


def get_melt_level(data, r, c):
    count = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if data[nr][nc] == 0:
                count += 1
    return count

def melt():
    copied_data = [row[:] for row in data]
    for i in range(n):
        for j in range(m):
            data[i][j] = max(0, copied_data[i][j] - get_melt_level(copied_data, i, j))


time = 0

while True:
    count = 0
    melt()
    time += 1
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0 and not visited[i][j]:
                bfs(visited, i, j)
                count += 1

    if count >= 2:
        print(time)
        break
    if is_all_melt():
        print(0)
        break


