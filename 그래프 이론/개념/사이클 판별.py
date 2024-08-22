"""
input : 첫줄은 노드와 간선의 개수
3 3
1 2
1 3
2 3

output
사이클이 발생했습니다.
"""

import sys
input = sys.stdin.readline

n, v = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
	parent[i] = i

def find_parent(parent, x):
	if (parent[x] != x):
		parent[x] = find_parent(parent, parent[x])
	return (parent[x])

def union(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if (a < b):
		parent[b] = a
	else:
		parent[a] = b

cycle = False

for _ in range(v):
	a, b = map(int, input().split())
	if (find_parent(parent, a) == find_parent(parent, b)):
		cycle = True
		break
	else:
		union(parent, a, b)

if (cycle):
	print("사이클이 발생했습니다.")
else:
	print("사이클이 발생하지 않았습니다.")
