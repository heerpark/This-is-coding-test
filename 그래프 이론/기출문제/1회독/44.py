"""
point

아직 모르겠다 ~~

input

5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19

"""

import sys

input = sys.stdin.readline

N = int(input())

x = []
y = []
z = []

graph = []

for i in range(1, N+1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

# print(x)
# print(y)
# print(z)

for i in range(1, N):
    graph.append((abs(x[i][0] - x[i-1][0]), x[i][1], x[i-1][1]))
    graph.append((abs(y[i][0] - y[i - 1][0]), y[i][1], y[i - 1][1]))
    graph.append((abs(z[i][0] - z[i - 1][0]), z[i][1], z[i - 1][1]))

graph.sort()

parent = [0] * (N + 1)

for i in range(1, N+1):
    parent[i] = i


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

result = 0

for i in graph:
    cost = i[0]
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        result += cost
        union_parent(parent, i[1], i[2])

print(result)