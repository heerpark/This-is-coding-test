from collections import deque


#board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
board = [[0, 0, 1, 1], [0, 0, 1, 1], [1, 0, 0, 1], [1, 0, 0, 0]]


def is_valid(board, r1, c1, r2, c2, n):
    if not (0 <= r1 < n and 0 <= c1 < n):
        return False
    if not (0 <= r2 < n and 0 <= c2 < n):
        return False
    if board[r1][c1] == 1 or board[r2][c2] == 1:
        return False
    return True


def bfs(board, n):
    q = deque()
    visited = set()  # ✅ 방문한 상태 저장용 집합
    start = ((0, 0), (0, 1))

    q.append((start[0], start[1], 0))  # 두 좌표와 시간
    visited.add(start)  # 초기 상태 추가

    while q:
        now = q.popleft()
        r1, c1 = now[0]
        r2, c2 = now[1]
        time = now[2]

        # 목표지점 도착
        if (r1 == n - 1 and c1 == n - 1) or (r2 == n - 1 and c2 == n - 1):
            return time

        # 이동할 수 있는 방향들
        moves = []

        # 위
        if is_valid(board, r1 - 1, c1, r2 - 1, c2, n):
            moves.append(((r1 - 1, c1), (r2 - 1, c2)))
        # 아래
        if is_valid(board, r1 + 1, c1, r2 + 1, c2, n):
            moves.append(((r1 + 1, c1), (r2 + 1, c2)))
        # 오른쪽
        if is_valid(board, r1, c1 + 1, r2, c2 + 1, n):
            moves.append(((r1, c1 + 1), (r2, c2 + 1)))
        # 왼쪽
        if is_valid(board, r1, c1 - 1, r2, c2 - 1, n):
            moves.append(((r1, c1 - 1), (r2, c2 - 1)))

        # 회전 (가로)
        if r1 == r2:
            for d in [-1, 1]:  # 위, 아래로 회전
                if is_valid(board, r1 + d, c1, r2 + d, c2, n):
                    moves.append(((r1, c1), (r1 + d, c1)))
                    moves.append(((r2 + d, c2), (r2, c2)))

        # 회전 (세로)
        elif c1 == c2:
            for d in [-1, 1]:  # 왼, 오른쪽으로 회전
                if is_valid(board, r1, c1 + d, r2, c2 + d, n):
                    moves.append(((r1, c1), (r1, c1 + d)))
                    moves.append(((r2, c2 + d), (r2, c2)))

        # 가능한 다음 위치들을 큐에 넣기
        for next_pos in moves:
            pos1, pos2 = next_pos
            # ✅ 좌표를 정렬해서 중복 방지 (같은 위치지만 순서가 바뀐 경우)
            sorted_pos = tuple(sorted([pos1, pos2]))
            if sorted_pos not in visited:
                visited.add(sorted_pos)
                q.append((sorted_pos[0], sorted_pos[1], time + 1))


def solution(board):
    n = len(board)
    answer = bfs(board, n)
    return answer



def solution(board):
    n = len(board)
    answer = bfs(board, n)
    return answer


print(solution(board))
