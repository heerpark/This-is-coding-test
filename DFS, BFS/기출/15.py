"""
input
4 4 1 1
1 2
1 3
2 3
2 4

point
graph를 직접 만들어서 사용
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
shortest = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start):
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                shortest[i] = shortest[now] + 1
                visited[i] = True
                q.append(i)

bfs(graph, x)
result = []
for i in range(1, n+1):
    if shortest[i] == k:
        result.append(i)

result.sort()
if not result:
    print(-1)
else:
    for i in result:
        print(i)
