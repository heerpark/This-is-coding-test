import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
b = []
e = []

for i in range(n):
    now = []
    data = input()
    for j in range(n):
        if data[j] == 'B':
            b.append((i, j))
            now.append(0)
        elif data[j] == 'E':
            e.append((i, j))
            now.append(0)
        elif data[j] == '0':
            now.append(0)
        elif data[j] == '1':
            now.append(1)
    graph.append(now)

# start, end - (type, row, col)
# 가로: 0 세로: 1
if b[1][0] == b[0][0]:
    start = (0, b[1][0], b[1][1], 0)
else:
    start = (1, b[1][0], b[1][1], 0)

if e[1][0] == e[0][0]:
    end = (0, e[1][0], e[1][1])
else:
    end = (1, e[1][0], e[1][1])

def is_valid(graph, state):
    if state[0] == 0:
        r1 = state[1]
        c1 = state[2] - 1
        r2 = state[1]
        c2 = state[2]
        r3 = state[1]
        c3 = state[2] + 1
    else:
        r1 = state[1] + 1
        c1 = state[2]
        r2 = state[1]
        c2 = state[2]
        r3 = state[1] - 1
        c3 = state[2]
    if not (0 <= r1 < n and 0 <= c1 < n and graph[r1][c1] == 0):
        return False
    if not (0 <= r2 < n and 0 <= c2 < n and graph[r2][c2] == 0):
        return False
    if not (0 <= r3 < n and 0 <= c3 < n and graph[r3][c3] == 0):
        return False
    return True


def can_rotate(graph, r, c):
    if not (1 <= r < n - 1 and 1 <= c < n - 1):
        return False
    if graph[r-1][c-1] == 1:
        return False
    if graph[r-1][c] == 1:
        return False
    if graph[r-1][c+1] == 1:
        return False
    if graph[r][c-1] == 1:
        return False
    if graph[r][c+1] == 1:
        return False
    if graph[r+1][c-1] == 1:
        return False
    if graph[r+1][c] == 1:
        return False
    if graph[r+1][c+1] == 1:
        return False
    return True


def bfs(graph, start, end):
    q = deque()
    visited = set()
    q.append(start)
    visited.add(start)
    while q:
        moves = []
        now = q.popleft()
        type, r, c, time = now
        # 위
        moves.append((type, r + 1, c, time + 1))
        # 아래
        moves.append((type, r - 1, c, time + 1))
        # 왼쪽
        moves.append((type, r, c - 1, time + 1))
        # 오른쪽
        moves.append((type, r, c + 1, time + 1))
        #회전
        if can_rotate(graph, r, c):
            if type == 0:
                moves.append((1, r, c, time + 1))
            else:
                moves.append((0, r, c, time + 1))
        for move in moves:
            type, r, c, time = move
            if (type, r, c) == end:
                return time
            state = (type, r, c)
            if is_valid(graph, state) and state not in visited:
                q.append((type, r, c, time))
                visited.add((type, r, c))
    return 0

result = bfs(graph, start, end)
print(result)
