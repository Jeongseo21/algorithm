import collections

numbers = [1,1,1,1,1]
target = 3

answer = 0
stack = collections.deque([(0, 0)])
while stack:
    curr_sum, num_idx = stack.popleft()

    if num_idx == len(numbers):
        if curr_sum == target:
            answer += 1
    else:
        number = numbers[num_idx]
        stack.append((curr_sum+number, num_idx+1))
        stack.append((curr_sum-number, num_idx+1))
print(answer)