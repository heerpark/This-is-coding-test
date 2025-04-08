import sys

n = int(input())

graph = [[0] * n for _ in range(n)]

data = [[] for _ in range(n**2)]
order = []

for _ in range(n**2):
    student, l1, l2, l3, l4 = map(int, input().split())
    order.append(student)
    data[student - 1].append(l1)
    data[student - 1].append(l2)
    data[student - 1].append(l3)
    data[student - 1].append(l4)


def is_adjacent(r1, c1, r2, c2):
    if abs(r1 - r2) + abs(c1 - c2) == 1:
        return True
    else:
        return False


def rule1_util(student, r, c):
    count = 0
    for i in range(n):
        for j in range(n):
            if is_adjacent(r, c, i, j):
                if graph[i][j] in data[student-1]:
                    count += 1
    return count


def rule1(student):
    temp = []
    result = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                count = rule1_util(student, i, j)
                temp.append((count, i, j))
    temp.sort(reverse=True)
    check = temp[0][0]
    for i in temp:
        if i[0] == check:
            result.append((i[1], i[2]))
            check = i[0]
        else:
            break
    return result


def get_adjacent_empty_count(r, c):
    count = 0
    for i in range(n):
        for j in range(n):
            if is_adjacent(r, c, i, j) and graph[i][j] == 0:
                count += 1
    return count


def rule2(result):
    temp = []
    rule2_result = []
    for r, c in result:
        count = get_adjacent_empty_count(r, c)
        temp.append((count, r, c))
    temp.sort(reverse=True)
    check = temp[0][0]
    for i in temp:
        if i[0] == check:
            rule2_result.append((i[1], i[2]))
            check = i[0]
        else:
            break
    return rule2_result


def rule3(result):
    sorted_result = sorted(result, key=lambda x: (x[0], x[1]))
    return sorted_result[0]


for i in order:
    rule1_result = rule1(i)
    if len(rule1_result) > 1:
        rule2_result = rule2(rule1_result)
        if len(rule2_result) > 1:
            r, c = rule3(rule2_result)
            graph[r][c] = i
        else:
            r = rule2_result[0][0]
            c = rule2_result[0][1]
            graph[r][c] = i
    else:
        r = rule1_result[0][0]
        c = rule1_result[0][1]
        graph[r][c] = i


def get_point(student, r, c):
    count = 0
    result = 0
    for i in range(n):
        for j in range(n):
            if is_adjacent(r, c, i, j):
                if graph[i][j] in data[student-1]:
                    count += 1
    if count == 1:
        result = 1
    elif count == 2:
        result = 10
    elif count == 3:
        result = 100
    elif count == 4:
        result = 1000
    return result



result = 0
for i in range(n):
    for j in range(n):
        result += get_point(graph[i][j], i, j)

print(result)



