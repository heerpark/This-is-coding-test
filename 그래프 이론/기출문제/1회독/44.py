"""
point
크루스칼 알고리즘의 사용할 edge정보들을 만들 때 Tiem out이 발생하지 않게, 효율적으로 만드는게 포인트
한 축을 정렬해서 n-1개의 edge를 뽑으면 x축 기준 최소 신장 트리를 만들 수 있다.
같은 방식으로 y, z축에서 edge를 뽑으면 3(n-1)개의 edge들이 있고 이 edge들로 global optimal solution을 찾으면 된다.

p.s.
사실 각 축의 최선의 정보들을 가지고 크루스칼 알고리즘을 돌리는게 왜 전역적인 정답을 보장하는지 설명못하겠음.
x축: a-c = 10 b-c = 5, y축: a-b = 1, b-c = 1 이라는 정보가 있을 때
x축에서 a-c = 10이라는 정보는 edge에 포함되지만, 더 짧은 y축의 a-c = 2라는 정보는 edge에 포함되지 않는 상황들 때문에 고민했음.
그냥 이런 경우 a-c라는 간선 자체가 선택되지 않고, a-b, b-c 로 최소 신장트리가 구성되기 때문에 global optimal solution이 보장된다고 생각하고 넘어감.

input
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19

output
4
"""

import sys

input = sys.stdin.readline

N = int(input())

x = []
y = []
z = []

graph = []

for i in range(1, N+1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

# print(x)
# print(y)
# print(z)

for i in range(1, N):
    graph.append((abs(x[i][0] - x[i-1][0]), x[i][1], x[i-1][1]))
    graph.append((abs(y[i][0] - y[i - 1][0]), y[i][1], y[i - 1][1]))
    graph.append((abs(z[i][0] - z[i - 1][0]), z[i][1], z[i - 1][1]))

graph.sort()

parent = [0] * (N + 1)

for i in range(1, N+1):
    parent[i] = i


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0

for i in graph:
    cost = i[0]
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        result += cost
        union_parent(parent, i[1], i[2])

print(result)