"""
input: 첫줄은 노드와 간선, 이후는 간선과 비용 
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

output
159
"""

n, v = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
	parent[i] = i

edge = []
for _ in range(v):
	a, b, cost = map(int, input().split())
	edge.append((cost, a, b))

edge.sort()

print(edge)

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

total = 0

for i in range(v):
	if (find_parent(parent, edge[i][1]) != find_parent(parent, edge[i][2])):
		total += edge[i][0]
		union(parent, edge[i][1], edge[i][2])

print(total)