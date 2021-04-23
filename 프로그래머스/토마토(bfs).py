import numpy as np
from collections import deque
import sys

sys.stdin = open("./input_file.txt", "r")


dq = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
graph = []

#그래프 입력받아 그리기

for n in range(N):
    graph.append(list(map(int, input().split())))
    for m in range(M):
        if graph[n][m] == 1:
            dq.append((n, m))
date = 0

def bfs(dq):
    temp = deque()
    while dq:
        y, x = dq.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == -1:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                temp.append((ny, nx))
    return temp


temp = bfs(dq)
while temp:
    date += 1
    temp = bfs(temp)


for n in range(N):
    for m in range(M):
        if graph[n][m] == 0:
            date = -1
            break
    if date == -1:
        break

print(date)


