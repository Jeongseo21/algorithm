from collections import deque

n = 6
computers = 	[[1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1]]

answer = 0
visited = [False for _ in range(n)]

def BFS():
    while dq:
        current = dq.popleft()
        for connect in range(n):
            if visited[connect] == False and computers[current][connect] == 1:
                visited[connect] = True
                dq.append(connect)

dq = deque([0])
for idx in range(n):
    if not visited[idx]:
        dq.append(idx)
        BFS()
        answer += 1



print(visited)
print(answer)
