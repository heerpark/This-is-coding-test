import  heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = 6, 11
start = 1
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b,c))

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q:
		dist, now = heapq.heappop(q)
		if dist > distance[now]:
			continue
		for i in graph[now]:
			new = dist + i[1]
			if new < distance[i[0]]:
				distance[i[0]] = new
				heapq.heappush(q, (new, i[0]))