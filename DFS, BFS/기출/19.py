"""
point

기본적인 dfs
"""

n = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))
num_count = len(number)
min_res = int(1e9 + 1)
max_res = -int(1e9 + 1)

def dfs(operator, depth, arr):
    global min_res, max_res
    if depth == num_count - 1:
        temp = number[0]
        for i in range(1, num_count):
            if arr[i-1] == 0:
                temp += number[i]
            elif arr[i-1] == 1:
                temp -= number[i]
            elif arr[i-1] == 2:
                temp  *= number[i]
            else:
                if temp < 0:
                    temp = -(abs(temp) // number[i])
                else:
                    temp = temp // number[i]
        min_res = min(min_res, temp)
        max_res = max(max_res, temp)
    else:
        for i in range(4):
            if operator[i] > 0:
                operator[i] -= 1
                arr.append(i)
                dfs(operator, depth+1, arr)
                operator[i] += 1
                arr.pop()

dfs(operator, 0, [])
print(max_res)
print(min_res)
