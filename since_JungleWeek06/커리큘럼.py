# 큐에 들어오는 순간 먼저 와있는 애들의 시간의 합 + 내 시간 = 최소 시간

import sys
from collections import deque
sys.stdin = open("input.txt", "r")

waiting_queue = deque()

N = int(input())

cost = [0]*(N+1)
indegree = [0]*(N+1)
done = []
graph = [[] for _ in range(N+1)]

flag = 0
for i in range(1, N+1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def pop_zero_indegree(indegree, waiting_queue):
    for i in range(1, N+1):
        if indegree[i] == 0:
            waiting_queue.append(i)
pop_zero_indegree(indegree, waiting_queue)

while waiting_queue:
    now = waiting_queue.pop()
    pointed = graph[now]
    for to in pointed:
        indegree[to] -= 1
        print(indegree)
    done.append(now)
    pop_zero_indegree(indegree, waiting_queue)
    print(waiting_queue)





