# 최소힙을 만들어놓고 D1 명령이 들어올 때 마다 최대힙으로 만들어준다..ㅎㅎ

import heapq

operations = 	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
count = 0
heap = []
max_heap = []

while count < len(operations):
    now = operations[count].split(' ')
    if now[0] == 'I':
        heapq.heappush(heap, int(now[1]))
        # print("insert", end=' ')
        # print(heap)
    elif now == ['D', '1']:
        if heap:
            max_heap = []
            for value in heap:
                heapq.heappush(max_heap, value * -1)
            heapq.heappop(max_heap)
            heap = []
            if max_heap:
                for value in max_heap:
                    heapq.heappush(heap, value * -1)
            # print("delete 1", end=' ')
            # print(heap)
    elif now == ['D', '-1']:
        if heap:
            heapq.heappop(heap)
        # print("delete -1", end=' ')
        # print(heap)
    count += 1

if heap:
    heap.sort()
    print([heap[-1], heap[0]])
else:
    print([0,0])

