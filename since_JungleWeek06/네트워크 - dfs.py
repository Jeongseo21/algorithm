# 네트워크 - dfs 풀이

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

visited = [False for _ in range(n)]
start = 0
answer = 0

def dfs(i):
    visited[i] = True
    for j in range(i+1, n):
        if computers[i][j] == 1 and not visited[j]:
            dfs(j)

cnt = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

