"""
point: 압축 find_parent에서의 return 값들, union에서 a = find_parent(parent, a)로 하는이유(parent_a = find_parent가 아니라)

input: 첫 줄은 노드의 개수와 간선 개수, 다음 줄 부터 간선
6 4
1 4
2 3
2 4
5 6

output
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 1 1 5 5

ps. 개선된 find_parent에서 각 원소가 속한 집합 출력안하고 그냥 부모테이블 출력하면 1 1 2 1 5 5 이렇게 나옴.
	원소가 속한 집합 출력하는 과정에서 parent 리스트 수정돼서 1 1 1 1 5 5 나오는 거임.
"""

import sys
input = sys.stdin.readline

n, v = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n+1):
	parent[i] = i

# def find_parent(parent, x):
# 	if parent[x] != x:
# 		return find_parent(parent, parent[x])
# 	return x

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

for _ in range(v):
	a, b = map(int, input().split())
	union_parent(parent, a, b)
