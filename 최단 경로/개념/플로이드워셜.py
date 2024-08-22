import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = 4, 7

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if i == j:
			graph[i][j] = 0

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a][b] = c

"""
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""


for k in range(1, n + 1):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

print(graph)

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if graph[i][j] != INF:
			print(graph[i][j], end=' ')
		else:
			print("INF")
	print()