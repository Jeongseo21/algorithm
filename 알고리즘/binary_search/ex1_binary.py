# 부품탐색 - binary search를 사용한 방법

# 이진탐색 구현
def binary_search(array, target, start, end):
    array.sort() #이진탐색을 사용하려면 반드시 정렬된 상태에서 탐색해야함
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

# 부품의 개수와 부품 번호 입력
N = int(input('N >> '))
N_array = list(map(int, input('N_array >> ').split()))
# 손님이 요청한 부품의 개수와 부품 번호 입력
M = int(input('M >> '))
M_array = list(map(int, input('M_array >> ').split()))

# 손님이 요청한 부품 확인하기
for m in M_array:
    # 해당부품이 존재하는지 탐색
    result = binary_search(N_array, m, 0, N-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')