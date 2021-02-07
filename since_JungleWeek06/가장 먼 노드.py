import sys
import heapq

n = 6

INF = 1e9

heapq_list = []

result = [0]+[INF]*(n)

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

edge = [[3, 6], [4, 3], [5, 2], [1, 3], [1, 5], [3, 5], [5, 6]]

for a, b in edge:
    graph[a].append((a, b))
    graph[b].append((b, a))

result[1] = 0
for i in range(len(graph[1])):
    heapq.heappush(heapq_list, graph[1][i])
    visited[1] = True

while(heapq_list):
    print(heapq_list)
    from_, to_ = heapq.heappop(heapq_list)
    if visited[to_] == True:
        continue
    if result[from_]+1 < result[to_]:
        result[to_] = result[from_]+1
    for i in range(len(graph[to_])):
        heapq.heappush(heapq_list, graph[to_][i])
    visited[to_] = True

max_num = max(result)
count = 0
for num in result:
    if num == max_num:
        count += 1
print(result)
print(count)



