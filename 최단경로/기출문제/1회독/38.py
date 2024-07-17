import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph1 = [[INF] * (n + 1) for _ in range(n + 1)]
graph2 = [[INF] * (n + 1) for _ in range(n + 1)]
graph3 = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if i == j:
			graph1[i][j] = 0
			graph2[i][j] = 0
			graph3[i][j] = 0

for _ in range(m):
	a, b = map(int, input().split())
	graph1[a][b] = 1
	graph2[b][a] = 1


for k in range(1, n + 1):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			graph1[i][j] = min(graph1[i][j], graph1[i][k] + graph1[k][j])
			graph2[i][j] = min(graph2[i][j], graph2[i][k] + graph2[k][j])

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if (graph1[i][j] != INF and graph1[i][j] != 0):
			graph3[i][j] = "+"
			print(graph3[i][j])
		if (graph2[i][j] != INF and graph2[i][j] != 0):
			graph3[i][j] = "-"

# print

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if graph1[i][j] == INF:
			print("X", end=" ")
		else:
			print(graph1[i][j], end=" ")
	print()

print("----------")
for i in range(1, n + 1):
	for j in range(1, n + 1):
		if graph2[i][j] == INF:
			print("X", end=" ")
		else:
			print(graph2[i][j], end=" ")
	print()

print("----------")
for i in range(1, n + 1):
	for j in range(1, n + 1):
		if graph3[i][j] == INF:
			print("X", end=" ")
		else:
			print(graph3[i][j], end=" ")
	print()

#print result
res = 0

for i in range(1, n + 1):
	flag = 0
	for j in range(1, n + 1):
		if graph3[i][j] == INF:
			flag = 1
	if flag == 0:
		res += 1

print("result", res)
	



# input
"""
6 6
1 5
3 4 
4 2
4 6
5 2
5 4
"""

# 풀이
"""
입력받는 연결 정보 a,b 는 (1) a가 b보다 낮다는 정보이다. 이 정보는 (2) b가 a보다 낮다는 정보도 내포한다.
(1)로 연결된 2차원 그래프에서 플로이드 워셜 알고리즘을 적용한 후 도달할 수 있는 사람들은 자신보다 점수가 낮은 사람들이다.
같은 방법으로 (2)에서는 자신보다 점수가 높은 사람들을 찾을 수 있다.
그렇다면 결과는 다음과 같이 도출할 수 있다.
(1)에서 자신보다 점수가 낮은 사람들 수 + (2)에서 자신보다 점수가 높은 사람들 수 = n -1 이면 그 사람이 몇 등인지 정확하게 찾을 수 있다는 것을 의미한다.
따라서 위의 조건을 만족하는 행의 수를 정답으로 출력하면 된다. (각 행 = 한 사람)
"""