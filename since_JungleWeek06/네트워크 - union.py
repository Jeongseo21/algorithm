

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

n = 3
computers = [[1, 1, 0, 1, 1], [1, 1, 0 1, 0], [0, 0, 1]]
parents = [0 for _ in range(n)]

for i in range(n):
    parents[i] = i

for i in range(n):
    for j in range(i+1, n):
        if computers[i][j] == 1:
            union_parent(parents, i, j)

for i in range(n):
    find_parent(parents, i)

count = 0
tmp = -1
for p in parents:
    if p != tmp:
        tmp = p
        count += 1
print(count)
