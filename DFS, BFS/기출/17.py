"""
input
https://www.acmicpc.net/problem/18405

point
priority queue 와 queue의 콜라보레이션 ~~ psy ~~

- queue
from collections import deque
q = deque()
q.append
q.popleft()

- priority queue
import heapq
pq = []
heapq.heappush(pq, data)
heapq.heappop()
"""

import heapq
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
s, x, y = map(int, input().split())

time = 0
virus = 0
pq = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            heapq.heappush(pq, (graph[i][j], i, j))
            virus += 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while time < s:
    temp = 0
    q = deque()
    # print("start", virus, time)
    while virus > 0:
        v_type, r, c = heapq.heappop(pq)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 0:
                graph[nr][nc] = v_type
                temp += 1
                q.append((v_type, nr, nc))
        virus -= 1
    while q:
        v_type, r, c = q.popleft()
        heapq.heappush(pq, (v_type, r, c))

    # for i in range(n):
    #     print(graph[i])
    # print('-------------')
    virus = temp
    time += 1

print(graph[x-1][y-1])


