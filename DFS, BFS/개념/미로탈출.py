"""
input
5 6
101010
111111
000001
111111
111111

point
bfs는 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().strip())) for _ in range(n)]

drow = [0, 0, 1, -1]
dcol = [1, -1, 0, 0]
def bfs(data, row, col):
    q = deque()
    q.append((row, col))
    while q:
        row, col = q.popleft()
        for i in range(4):
            new_row = row + drow[i]
            new_col = col + dcol[i]
            if 0 <= new_row < n and 0 <= new_col < m and data[new_row][new_col] == 1:
                data[new_row][new_col] = data[row][col] + 1
                q.append((new_row, new_col))


bfs(data, 0, 0)
print(data[n-1][m-1])
