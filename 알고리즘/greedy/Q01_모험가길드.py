'''
잘못된 풀이))

N = 8
fears = [1, 2, 4, 2, 2, 1, 1, 3]

fears = sorted(fears, reverse=True)
count = 0

for i in fears:
    if i > len(fears):
        break
    elif i == len(fears):
        count += 1
        break
    fears = fears[i:]
    count += 1

print(count)
'''

N = 8
fears = [1, 2, 4, 2, 2, 1, 1, 3]
fears = sorted(fears)
count = 0
result = 0

for f in fears:
    count += 1
    if f == count:
        result += 1
        count = 0

print(result)
