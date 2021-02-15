import heapq

scoville = [0, 0]
K = 1

heaplist = []

for val in scoville:
    heapq.heappush(heaplist, val)

mix_cnt = 0
while heaplist[0] < K:
    try:
        heapq.heappush(heaplist, heapq.heappop(heaplist)+heapq.heappop(heaplist)*2)
    except IndexError:
        print(-1)
        break
    mix_cnt += 1
print(mix_cnt)