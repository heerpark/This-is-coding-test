def combination(arr, n, r, count, now):
    if count == r:
        print(arr)
        return
    for i in range(now + 1, n+1):
        arr.append(i)
        combination(arr, n, r, count+1, i)
        arr.pop()

combination([], 5, 3, 0, 0)
