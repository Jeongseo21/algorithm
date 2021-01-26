import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = [INF]*(n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_val = INF
    min_idx = 3
    for i in range(1, n+1):
        if not visited[i] and min_val > result[i]:
            min_val = result[i]
            min_idx = i
    return min_idx

# dijkstra
def dijkstra(start):
    # 시작 노드 초기화
    visited[start] = True
    result[start] = 0
    # 시작 노드를 제외한 전체 n-1 개의 노드 반복, result 갱신
    for i in range(len(graph[start])):
        node, val = graph[start][i]
        result[node] = val
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
    for i in range(1, n-1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인, 현재 노드를 거쳐서 다른 노드 방문할 때 더 거리가 짧은 경우 갱신
        for j in graph[now]:
            cost = result[now] + j[1]
            if cost < result[j[0]]:
                result[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
print(result)