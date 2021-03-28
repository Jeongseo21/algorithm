number = "98765"
k = 3

nums = list(map(int, number))
surviving = []
cnt = 0

while(cnt < k and len(nums) > 1):
    temp = nums.pop(0)

    if temp >= nums[0]:
        surviving.append(temp)
    else:
        cnt += 1
        while(surviving != [] and cnt < k):
            min_num = min(surviving)
            if min_num > nums[0]:
                break
            surviving.remove(min_num)
            cnt += 1

surviving.extend(nums)
if (k - cnt > 0):
    while cnt != k:
        min_num = min(surviving)
        surviving.remove(min_num)
        cnt += 1
new = list(map(str, surviving))
print("".join(new))




