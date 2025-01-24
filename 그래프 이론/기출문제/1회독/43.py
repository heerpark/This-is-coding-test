"""
point
그냥 기본 문제 포인트 없음 ㅅㄱ

input
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

output
51
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
data = []
for _ in range(M):
    x, y, z = map(int, input().split())
    data.append((z, x, y))

data.sort()

parent = [0] * (N + 1)

for i in range(1, N+1):
    parent[i] = i

total_cost = 0
min_cost = 0

for i in data:
    total_cost += i[0]
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        min_cost += i[0]
        union_parent(parent, i[1], i[2])

print(total_cost - min_cost)
