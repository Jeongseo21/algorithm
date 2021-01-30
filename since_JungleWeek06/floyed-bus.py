import sys
# import numpy
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
# graph = numpy.array(graph)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

# print(graph)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()