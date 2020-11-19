# 가까운 노드부터 탐색하는 알고리즘
# 큐를 사용함
# 시간 복잡도는 O(N)
# 일반적으로 실제 수행시간은 DFS보다 좋은 편

from collections import deque

#BFS메서드 정의
def bfs(graph, start, visited):
    # dequeue 라이브러리 사용
    queue = deque([start])
    # 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end='  ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

bfs(graph, 1, visited)