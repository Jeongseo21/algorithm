# DFS는 스택 자료구조에 기초한다.
# 재귀함수를 사용해서 간단하게 구현할 수 있다.
# 시간복잡도는 O(N)이다.

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='  ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)