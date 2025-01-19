"""
point
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

G = int(input())
P = int(input())

parent = [0] * (G + 1)
for i in range(1, G+1):
    parent[i] = i

end_count = 0
count = 0

for _ in range(P):
    g = int(input())
    count += 1
    union_parent(parent, g, g-1)
    if find_parent(parent, g) == 0:
        end_count += 1
        if end_count == 2:
            count -= 1

print(count)

