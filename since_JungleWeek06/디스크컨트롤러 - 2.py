import heapq

jobs = [[0, 10], [0, 3], [4, 10], [5, 11], [10, 3], [15, 2]]

count = 0 # 작업의 수
last = -1 # 최근 작업이 끝난 시각
answer = 0
heap = []
jobs.sort()

# 시작시간 초기화
time = jobs[0][0] # 총 작업 시간
while count < len(jobs):
    for s, t in jobs:
        if last < s <= time:
            heapq.heappush(heap, (t, s))
    # 바로 수행할 수 있는 작업이 있는 경우
    if len(heap) > 0:
        count += 1
        last = time
        term, start = heapq.heappop(heap)
        time += term
        answer += (time - start)
    else:
        time += 1
print(answer // len(jobs))