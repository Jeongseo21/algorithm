import sys
import heapq
input = sys.stdin.readline

N, M, C = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
result = [INF]*(N+1)
start = C

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Z, Y))

heaplist = []
heapq.heappush(heaplist, (0, start))
result[start] = 0

while heaplist:
    new = heapq.heappop(heaplist)
    visited[new[1]] = True
    for j in graph[new[1]]:
        cost = new[0] + j[0]
        if cost < result[j[1]]:
            result[j[1]] = cost
            heapq.heappush(heaplist, (result[j[1]], j[1]))
count = 0
max_num = 0
for i in range(len(result)):
    if result[i] == INF:
        continue
    count += 1
    if max_num < result[i]:
        max_num = result[i]
print(count-1, max_num)
print(result)