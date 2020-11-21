def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 타겟을 찾을 경우 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간값이 타겟보다 작은 경우
        elif array[mid] < target:
            start = mid + 1
        # 중간값이 타겟보다 큰 경우
        else:
            end = mid - 1
    return None

# 원소의 개수와 찾고자하는 원소 입력
n, target = list(map(int, input('n target >> ').split()))
# 전체 원소 입력
array = list(map(int, input('원소입력 >> ').split()))

# 이진탐색 수행결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1, end=' ')
    print('번째 원소가 '+ str(target) + ' 입니다.')

