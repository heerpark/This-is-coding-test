import sys
input = sys.stdin.readline
INF = int(1e9)

# n, m = map(int, input().split("n, m"))
# start = int(input("start"))
n, m = 6, 11
start = 1
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

#input
"""
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def get_smallest_node():
	min_value = INF
	min_node = 0
	for i in range(1, n + 1):
		if not visited[i]:
			if distance[i] < min_value:
				min_value = distance[i]
				min_node = i
	return (min_node)

def dijkstra(start):
	distance[start] = 0
	print(graph)
	for _ in range(n):
		now = get_smallest_node()
		print("loop!", now)
		visited[now] = True
		for i in graph[now]:
			cost = distance[now] + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost

dijkstra(start)
print(distance)