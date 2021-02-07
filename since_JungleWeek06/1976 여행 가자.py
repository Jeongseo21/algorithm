import sys

INF = int(1e9)
N = int(input())
M = int(input())
parents = [0]*(N+1)
plan = []
cycle = False

for i in range(1, N+1):
    parents[i] = i

def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    x = find_parents(parents, x)
    y = find_parents(parents, y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

graph = [[0]*(N+1)]
for i in range(N):
    graph.append([0]+list(map(int, input().split())))


plan = list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(i, N+1):
        if graph[i][j] == 1:
            union(parents, i, j)

for i in range(1, N+1):
    find_parents(parents, i)

for i in range(1, M):
    if parents[plan[i]] != parents[plan[i-1]]:
        cycle = False
        break
    else:
        cycle = True
if cycle:
    print("YES")
else:
    print("NO")
