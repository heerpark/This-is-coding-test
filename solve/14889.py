# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# result = int(1e9)
#
#
# n = int(input())
# data = []
#
# for _ in range(n):
#     data.append(list(map(int, input().split())))
#
# team = []
#
# def calculate(team):
#     global result
#     other_team = []
#     for i in range(n):
#         if i in team:
#             continue
#         else:
#             other_team.append(i)
#     team_score = 0
#     other_team_score = 0
#     for now in combinations(team, n//2):
#         for now2 in combinations(now, 2):
#             team_score += data[now2[0]][now2[1]]
#             team_score += data[now2[1]][now2[0]]
#     for now in combinations(other_team, n//2):
#         for now2 in combinations(now, 2):
#             other_team_score += data[now2[0]][now2[1]]
#             other_team_score += data[now2[1]][now2[0]]
#     result = min(result, abs(team_score - other_team_score))
#
#
# all_member = []
#
# for i in range(n):
#     all_member.append(i)
#
# for team in combinations(all_member, n//2):
#     calculate(team)
#
# print(result)
#

def combination(n, r, now):
    if len(now) == r:
        print(now)
        return
    for i in range(len(now), n):
        now.append(i)
        for j in range(i + 1, n):
            now.append(i)
            combination(n, r, now)
            now.pop()

combination(5, 3, [])
