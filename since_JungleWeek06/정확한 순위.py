import sys
# import numpy
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())


graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
#graph = numpy.array(graph)
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for i in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

for i in range(N+1):
    for j in range(N+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

result = [0 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] != 0:
            result[i] += 1
            result[j] += 1
answer = 0
for i in result:
    if i == N-1:
        answer += 1
print(answer)
