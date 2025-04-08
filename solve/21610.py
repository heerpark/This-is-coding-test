n, m = map(int, input().split())

graph = []
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

moves = []
for _ in range(m):
    d, s = map(int, input().split())
    moves.append((d, s))

cloud = [[False] * n for _ in range(n)]

cloud[n-1][0] = True
cloud[n-1][1] = True
cloud[n-2][0] = True
cloud[n-2][1] = True


def moved_coordinate(d, s, i, j):
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [-1, -1, 0, 1, 1, 1, 0, -1]
    new_i = i + dr[d-1] * s
    new_j = j + dc[d-1] * s
    while not (0 <= new_i < n):
        if new_i < 0:
            new_i += n
        else:
            new_i -= n
    while not (0 <= new_j < n):
        if new_j < 0:
            new_j += n
        else:
            new_j -= n
    return new_i, new_j


def move_clouds(cloud, d, s):
    bef = []
    new = []
    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                bef.append((i, j))
                new_i, new_j = moved_coordinate(d, s, i, j)
                new.append((new_i, new_j))
    for i, j in bef:
        cloud[i][j] = False
    for i, j in new:
        cloud[i][j] = True



def rain_and_copy_and_die(graph, cloud):
    temp = []
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]
    # 비내린다
    for i in range(n):
        for j in range(n):
            if cloud[i][j]:
                graph[i][j] += 1
                temp.append((i, j))
    # 물복사버그
    for i, j in temp:
        sum = 0
        for k in range(4):
            new_i = i + dr[k]
            new_j = j + dc[k]
            if 0 <= new_i < n and 0 <= new_j < n:
                if graph[new_i][new_j] > 0:
                    sum += 1
        graph[i][j] += sum

    # 구름 있는 칸 제외하고 물의 양이 2이상인 칸에 구름 만들기. 구름이 생기면 물의 양이 2만큼 준다.
    for i in range(n):
        for j in range(n):
            if not cloud[i][j]:
                if graph[i][j] >= 2:
                    cloud[i][j] = True
                    graph[i][j] -= 2
    # 뒤지기
    for i, j in temp:
        cloud[i][j] = False


def debug(graph, cloud):
    print("graph")
    for i in range(n):
        print(graph[i])
    print("cloud")
    for i in range(n):
        print(cloud[i])

def move(graph, cloud, d, s):
    move_clouds(cloud, d, s)
    rain_and_copy_and_die(graph, cloud)
    # debug(graph, cloud)


for d, s in moves:
    move(graph, cloud, d, s)

result = 0
for i in range(n):
    for j in range(n):
        result += graph[i][j]

print(result)