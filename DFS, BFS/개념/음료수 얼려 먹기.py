"""
input
4 5
00110
00011
11111
00000

result
3

point
구역의 개수를 어떻게 count 하는지
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = [list(map(int, input().strip())) for _ in range(n)]

def dfs(data, row, col):
    if row < 0 or row >= n or col < 0 or col >= m:
        return False
    if data[row][col] == 0:
        data[row][col] = 1
        dfs(data, row+1, col)
        dfs(data, row-1, col)
        dfs(data, row, col+1)
        dfs(data, row, col-1)
        return True
    return False

count = 0

for i in range(n):
    for j in range(m):
        if dfs(data, i, j):
            count += 1

print(count)


