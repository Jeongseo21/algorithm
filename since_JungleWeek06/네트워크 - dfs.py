# 네트워크 - dfs 풀이

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

visited = [False for _ in range(n)]
start = 0
answer = 0

def dfs(computers, visited, start):
    ready = [start]
    while ready:
        now = ready.pop(0)
        print(now)
        print(ready)
        if visited[now]:
            continue
        visited[now] = True
        for i in range(n):
            if computers[now][i] == 1 and visited[i]:
                ready.append(i)



while False in visited:
    if not visited[start]:
        dfs(computers, visited, start)
        answer += 1
    start += 1
print(answer)

