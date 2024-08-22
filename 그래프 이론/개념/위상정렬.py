

"""
point: 왜 여기서는 간선정보를 2차원 리스트로 저장할까.
input: 첫줄은 노드와 간선의 개수
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""

from collections import deque

n, v = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(1, v + 1):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1

def topology_sort():
	result = []
	q = deque()

	for i in range(1, n + 1):
		if indegree[i] == 0:
			q.append(i)

	while q:
		now = q.popleft()
		result.append(now)
		for i in graph[now]:
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)

	for i in result:
		print(i, end=' ')
	print()

topology_sort()
	 
