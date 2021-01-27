import sys
import heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = [INF]*(n+1)
heqlist = []

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

'''
# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_val = INF
    min_idx = 3
    for i in range(1, n+1):
        if not visited[i] and min_val > result[i]:
            min_val = result[i]
            min_idx = i
    return min_idx
'''
# dijkstra
def dijkstra(start):
    # 시작 노드 초기화
    result[start] = 0
    heapq.heappush(heqlist, (result[start], start))

    # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
    while heqlist:
        print(heqlist)
        now = heapq.heappop(heqlist)[1]
        if visited[now]:
            continue
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인, 현재 노드를 거쳐서 다른 노드 방문할 때 더 거리가 짧은 경우 갱신
        for j in graph[now]:
            cost = result[now] + j[0]
            if cost < result[j[1]]:
                result[j[1]] = cost
                heapq.heappush(heqlist, (cost, j[1]))


dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
print(result)