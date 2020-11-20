# 퀵정렬 시간복잡도는 O(NlogN)
# 평균적으로 엔로그엔이지만 최악의 경우 엔제곱
# 데이터가 이미 정렬되어있을수록 더 비효율적임

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    # 피봇은 0번째 원소
    pivot = array[0]
    # tail은 나머지 원소
    tail = array[1:]

    # pivot 보다 작으면 left_side, 크면 right_side
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))