import heapq

scoville = [100]
K = 7
time = 0
while True:
    if len(scoville) < 2:
        if scoville[0] < K:
            print(-1)
        else:
            print(0)
        break
    heapq.heapify(scoville)
    first = heapq.heappop(scoville)
    if first < K:
        time += 1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+second*2)
    else:
        print(time)
        break


'''
print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)
'''