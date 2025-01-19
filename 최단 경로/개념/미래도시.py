import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
data = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    data[s].append(e)
    data[e].append(s)

x, k = map(int, input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        now = heapq.heappop(q)
        if now[0] > distance[now[1]]:
            continue
        for i in data[now[1]]:
            cost = now[0] + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


dijkstra(1)
res = distance[k]
distance = [INF] * (n + 1)
dijkstra(k)
res += distance[x]

if res < INF:
    print(res)
else:
    print(-1)

