import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
q = []
N, M, C = map(int, input().split())
distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        now = heapq.heappop(q)
        if distance[now[1]] < now[0]:
            continue
        for i in graph[now[1]]:
            cost = now[0] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

city = 0
for i in range(1, N + 1):
    if distance[i] > 0:
        city += 1

max_time = max(distance[1:])

print(city, max_time)