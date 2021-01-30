import sys
import numpy
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
graph = numpy.array(graph)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])
print(graph)
