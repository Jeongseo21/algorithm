import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
result = [INF for _ in range(V+1)]
graph = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
heaplist = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

result[K] = 0
heapq.heappush(heaplist, (0, K))

while heaplist:
    now = heapq.heappop(heaplist)
    if visited[now[1]]:
        continue
    for j in graph[now[1]]:
        cost = now[0] + j[0]
        if cost < result[j[1]]:
            result[j[1]] = cost
            heapq.heappush(heaplist, (cost, j[1]))
    visited[now[1]] = True

for i in range(1, V+1):
    if result[i] == INF:
        result[i] = 'INF'

        
    print(result[i])




