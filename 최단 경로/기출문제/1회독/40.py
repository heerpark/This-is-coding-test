import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

INF = int(1e9)
distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append((e, 1))
    graph[e].append((s, 1))

q = []

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        now = heapq.heappop(q)
        if now[0] > distance[now[1]]:
            continue
        for i in graph[now[1]]:
            cost = now[0] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    max = -1
    max_idx = 0
    max_count = 0
    for i in range(1, len(distance)):
        if distance[i] > max:
            max = distance[i]
            max_idx = i
            max_count = 1
        elif distance[i] == max:
            max_count += 1
    print(max_idx, max, max_count)

dijkstra(1)

"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""