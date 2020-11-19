n, m = 3, 3

graph = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
    ]

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문하는 메서드
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우를 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1


print(result)
