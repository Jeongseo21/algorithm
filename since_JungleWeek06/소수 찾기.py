from itertools import permutations


def deci_check(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

numbers = "100"
permut = []
nums = []
count = 0
for i in range(len(numbers)+1):
    permut += list(permutations(numbers, i))

for num in permut:
    num = "".join(num)
    if num == '' or num == '0':
        continue
    else:
        nums.append(int(num))

nums = list(set(nums))
print(nums)

for num in nums:
    if deci_check(num):
        print(num)
        count += 1
print(count)
