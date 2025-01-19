import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def get_graph(N):
    data = []
    for _ in range(N):
        row = list(map(int, input().split()))
        data.append(row)
    graph = [[] for _ in range(N * N)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if x >= 0 and y >= 0 and x < N and y < N:
                    graph[x*N+y].append((i*N+j, data[i][j]))

    return graph, data[0][0]

def dijkstra(N):
    graph, start_cost = get_graph(N)
    distance = [INF] * (N * N)
    distance[0] = start_cost
    q = []
    heapq.heappush(q, (start_cost, 0))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            new = dist + i[1]
            if new < distance[i[0]]:
                distance[i[0]] = new
                heapq.heappush(q, (new, i[0]))
    print(distance[-1])

times = int(input())
for _ in range(times):
    n = int(input())
    dijkstra(n)




"""

3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

"""
