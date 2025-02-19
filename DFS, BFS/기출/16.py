"""
input
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

point
백트래킹을 통한 벽 세우기
"""

import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

def bfs():
    global result
    q = deque()
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    safe_zone = 0
    tmp_graph = [row[:] for row in graph]
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append((i, j))
    while q:
        r, c = q.popleft()
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < n and 0 <= new_c < m and tmp_graph[new_r][new_c] == 0:
                tmp_graph[new_r][new_c] = 2
                q.append((new_r, new_c))
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:
                safe_zone += 1
    result = max(result, safe_zone)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count + 1)
                graph[i][j] = 0

make_wall(0)
print(result)

