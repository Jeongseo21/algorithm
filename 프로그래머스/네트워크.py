from collections import deque

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(dq):
    while dq:
        y, x = dq.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if computers[ny][nx] == 1:
                dq.append((ny, nx))
                computers[ny][nx] = 0


for j in range(n):
    for i in range(j, n):
        if computers[j][i] == 1:
            answer += 1
            dq = deque([(j, i)])
            bfs(dq)

print(answer)