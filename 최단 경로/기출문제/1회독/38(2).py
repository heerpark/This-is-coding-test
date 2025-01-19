import heapq
import sys
input = sys.stdin.readline

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""

def print_graph(graph):
    n = len(graph)
    for i in range(1, n):
        for j in range(1, n):
            if graph[i][j] != INF:
                print(graph[i][j], end=' ')
            else:
                print('X', end=' ')
        print()

N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

result = 0

for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == N - 1:
        result += 1
print_graph(graph)
print(result)
