import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [0]*(N+1)

for i in range(N+1):
    parents[i] = i

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def check(a, b):
    if find_parent(parents, a) == find_parent(parents, b):
        print('YES')
    else:
        print('NO')

for i in range(M):
    order, a, b = map(int, input().split())
    if order == 0:
        union_parent(parents, a, b)
    elif order == 1:
        check(a, b)


