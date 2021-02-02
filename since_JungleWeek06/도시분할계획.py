import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
parents = [0] * (N+1)
graph = [[] for _ in range(N+1)]
heaplist = []
total_cost = 0
max_cost = 0


for i in range(1, N+1):
    parents[i] = i

for i in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(heaplist, (C, A, B))


def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union(x, y):
    x = find_parent(parents, x)
    y = find_parent(parents, y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

while heaplist:
    cost, fr, to = heapq.heappop(heaplist)
    if find_parent(parents, fr) == find_parent(parents, to):
        continue
    union(fr, to)
    total_cost += cost
    if max_cost < cost:
        max_cost = cost

print(total_cost-max_cost)

