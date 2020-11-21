# H가 조건을 만족하는지 검사
'''
순차탐색으로 구현한 코드이다.
그러나 문제에서 절단기의 높이(H)가 최대 10억까지의 정수라는 조건이 있기 때문에
순차탐색은 시간초과가 나올 것이다.
10억까지의 정수라는 조건을 보고 이진탐색을 떠올려야 한다.
'''
'''
# 코드

def check(array, N, M, H):
    result = []
    for x in array:
        if x > H:
            result.append(x - H)
        else:
            result.append(0)
    if sum(result) < M:
        return None
    else:
        return H


N = int(input('N:떡의 개수 >> '))
M = int(input('M:요청한 떡의 길이 >> '))
array = list(map(int, input('array:떡의 개별 높이 >> ').split()))

max_num = max(array) - 1
for i in range(max_num, 0, -1):
    if check(array, N, M, i) != None:
        print(check(array, N, M, i))
        break
'''
# 이진탐색으로 구현

N = int(input('N:떡의 개수 >> '))
M = int(input('M:요청한 떡의 길이 >> '))
array = list(map(int, input('array:떡의 개별 높이 >> ').split()))

max_num = max(array)
start = 0
end = max_num
target = M

result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < target:
        end = mid -1
    else:
        result = mid
        start = mid +1
print(result)



