"""
point
가장 긴 증가하는 부분수열의 개념 사용


input
7
15 11 4 8 5 2 4
"""

import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

dp = [1] * (N)

for i in range(len(data)):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))