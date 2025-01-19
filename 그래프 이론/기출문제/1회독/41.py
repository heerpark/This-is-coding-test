"""
input

5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""

import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
graph = []
for _ in range(N):
    data = list(map(int, input().split()))
    graph.append(data)

parent = [0] * (N + 1)

for i in range(1, N+1):
    parent[i] = i

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)

data = list(map(int, input().split()))

flag = 0

for i in range(1, M):
    if find_parent(parent, data[i]) != find_parent(parent, data[i-1]):
        flag = 1
        print("NO")
        break
if not flag:
    print("YES")
