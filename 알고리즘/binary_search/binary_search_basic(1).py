# 단계를 거칠수록 확인해야할 데이터의 개수가 절반으로 줄어든다. O(logN)
# 탐색의 범위가 2000만을 넘어가는 경우 이진 탐색으로 문제에 접근해보기
# 처리해야할 데이터의 값이 1000만의 넘어가는 경우에는 시간복잡도가 O(logN)인 알고리즘을 떠올려보기


def binary_search(array, target, start, end):
    # start가 end보다 크면 None 리턴
    if start > end:
        return None

    # 중간점 찾기
    mid = (start + end) // 2

    # 중간점이 찾고자 하는 값이면 return
    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)

    else:
        return binary_search(array, target, mid+1, end)

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