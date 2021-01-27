import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e9)
# n, m 받기
n, m = map(int, input().split())
# start 받기
start = int(input())
# graph 생성
graph = [[] for _ in range(n+1)]
# result 생성
result = [INF]*(n+1)
# visited 생성
visited = [False]*(n+1)

# get_now() 생성
def get_now(result):
    min_val = INF
    for i in range(1, len(result)):
        if not visited[i] and min_val > result[i]:
            min_val = result[i]
            min_idx = i
    print(min_idx)
    return min_idx

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
print(graph)

def dijkstra(start):
    # 초기 세팅
    result[start] = 0
    for startlist in graph[start]:
        print(startlist)
        result[startlist[0]] = startlist[1]
    visited[start] = True
    print(result)
    for i in range(1, n+1):
        now = get_now(result)
        visited[now] = True
        for values in graph[now]:
            cost = result[now] + values[1]
            if cost < result[values[0]]:
                result[values[0]] = cost
            print(result)

dijkstra(start)