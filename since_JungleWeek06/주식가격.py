from collections import deque

prices = [1, 2, 3, 2, 3]
result = [0] * len(prices)

for i in range(len(prices)):
    for j in range(0, i):
        if prices[i] >= prices[j]:
            result[j] += 1
print(result)

'''
from collections import deque

def solution(prices):
    
    result = []

    for i in range(len(prices)):
        check = prices[i:len(prices)]
        dq = deque(check)
        start = dq.popleft()
        count = 0
        while dq:
            value = dq.popleft()
            if value < start:
                count += 1
                break
            count += 1
        result.append(count)
    
    return result
'''