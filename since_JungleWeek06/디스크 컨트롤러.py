import heapq

jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]
time = 0
answer = 0
ready = []
jobs_len = len(jobs)
last = -1
count = 0

jobs.sort()

time = jobs[0][0]
while count < jobs_len:
    for start, length in jobs:
        if last < start <= time:
            heapq.heappush(ready, (length, start))
    if ready:
        count += 1
        last = time
        term, start = heapq.heappop(ready)
        time += term
        answer += time - start
    else:
        time += 1
print(answer // jobs_len)

