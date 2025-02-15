import sys

input = sys.stdin.readline

n = int(input())
data= []
dp = [0] * 500
for _ in range(n):
    line = list(map(int, input().split()))
    data.append(line)

dp[0] = data[0][0]
idx = 0

for i in range(1, n):
    for j in range(len(data[i])):
        dp[idx + i] = max(dp[idx+i], dp[idx] + data[i][j])
        dp[idx + i + 1] = max(dp[idx+i+1], dp[idx] + data[i][j])
        print(idx + i, idx + i + 1)
        idx += 1

print(data)
print(dp)