"""
point

Graph 파트에서 가장 어려운 문제
1. 위상정렬을 통해 순위를 매기는 아이디어를 떠올려야 함.
2. 위상정렬을 떠올렸으면, 문제의 정보를 graph로 변활할 수 있어야함.
3. 처음 만든 graph에서 순위 변동이 있을 때, 어떻게 graph를 조작할 지 생각해야함.
4. 위상정렬에서 cycle이 발생한 case, 큐에 두 개가 삽입되는 case가 무엇을 의미하는 지 알아야함.

input
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3

"""

import sys
from collections import deque
input = sys.stdin.readline


def get_data(n):
    data = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            graph[data[i]].append(data[j])
            indegree[data[j]] += 1
    # print("org graph", graph)
    # print("org indegree", indegree)
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if data.index(a) < data.index(b):
            indegree[a] += 1
            indegree[b] -= 1
            graph[a].remove(b)
            graph[b].append(a)
        else:
            indegree[a] -= 1
            indegree[b] += 1
            graph[b].remove(a)
            graph[a].append(b)
    return graph, indegree

def topology_sort(n):
    graph, indegree = get_data(n)
    print(graph)
    print(indegree)
    q = deque()
    result = []
    append_count = 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            append_count += 1
            q.append(i)
    if append_count > 1:
        return [-1]
    while q:
        append_count = 0
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                append_count += 1
        if append_count > 1:
            return [-1]
    if len(result) < n:
        return [-2]
    return result

n = int(input())
for _ in range(n):
    x = int(input())
    result = topology_sort(x)
    if result[0] == -1:
        print("?")
    elif result[0] == -2:
        print("IMPOSSIBLE")
    else:
        for i in result:
            print(i, end=' ')
        print()

# x = int(input())
# result = topology_sort(x)
# if result[0] == -1:
#     print("?")
# elif result[0] == -2:
#     print("IMPOSSIBLE")
# else:
#     for i in result:
#         print(i, end=' ')
#     print()

