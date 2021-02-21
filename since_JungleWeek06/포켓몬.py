from itertools import permutations

nums = [3,3,3,2,2,4]
len_nums = len(nums)
nPr = permutations(nums, len_nums//2)
cases = list(nPr)
answer = 0

for case in cases:
    temp = len(set(case))
    if temp > answer:
        answer = temp
print(answer)