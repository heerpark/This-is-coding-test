import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, l, r = map(int, input().split())
data = []
drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

for _ in range(n):
    data.append(list(map(int, input().split())))