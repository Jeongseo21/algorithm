from collections import deque

numbers = [1, 1, 1, 1, 1]
target = 3
answer = 0
dq = deque([(0, 0)])

while dq:
    current, idx = dq.popleft()
    if idx == len(numbers):
        if current == target:
            answer += 1
    else:
        dq.append((current + numbers[idx], idx+1))
        dq.append((current - numbers[idx], idx+1))

print(answer)
