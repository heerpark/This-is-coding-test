"""
1차원 리스트 초기화 할 때 [] * (N + 1)로하면 N+1개의 원소로 초기화 안됨. [0] * (N + 1) 이런식으로 해야함. []를 N+1개로 복사하는데 []는 아무것도 없기 때문.

input

7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

output
NO
NO
YES
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

parent = [0] * (N + 1)

for i in range(N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b= find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    type, a, b = map(int, input().split())
    if type == 0:
        union_parent(parent, a, b)
    elif type == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")