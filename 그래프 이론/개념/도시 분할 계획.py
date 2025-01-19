"""
input

7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

output

8
"""

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

parent = [0] * (N + 1)
data = []

for i in range(1, N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    a, b, cost = map(int, input().split())
    data.append((cost, a, b))

data.sort()
result = []

for i in data:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        union_parent(parent, i[1], i[2])
        result.append(i[0])

result.sort()
print(sum(result[:-1]))