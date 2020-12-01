'''
완전탐색 문제
- ex2. 시각
'''
count = 0

N = int(input('N >> '))
for i in range(N+1):
    for j in range(59+1):
        for k in range(59+1):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

'''
for i in range(N+1):
    if '3' in i:
        count += 1
        continue
    for j in range(59+1):
        if '3' in j:
            count += 1
            continue
        for k in range(59+1):
            if '3' in j:
            count += 1
            continue

위의 코드는 k를 0-60까지 반복한 후 j를 1 증가시키고 다시 k를 0-60 반복하고 다시 j를 1 증가시키고 다시 k를 0-60 반복하는 식으로 작동한다.
따라서 위 코드로는 아이디어를 그대로 구현할 수 없다.
'''