"""
point

본인이 0이 됐을 때의 시간을 같이 넣자

input

5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

output
10
20
14
18
17

"""

from collections import deque
import sys

input = sys.stdin.readline
q = deque()

N = int(input())

graph = [[] for _ in range(N + 1)]
time = [0] * (N + 1)
indegree = [0] * (N + 1)

for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if j == 0:
            time[i] = data[j]
        elif data[j] != -1:
            indegree[i] += 1
            graph[data[j]].append(i)

# print(time)
# print(indegree)
# print(graph)

def topology_sort():
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append((i, 0))
    while q:
        now = q.popleft()
        time[now[0]] += now[1]
        for i in graph[now[0]]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, time[now[0]]))
    for i in range(1, N+1):
        print(time[i])

topology_sort()

