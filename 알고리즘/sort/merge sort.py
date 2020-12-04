'''
merge sort
n/2로 나누고, 1개씩의 요소가 남을 때까지 재귀적으로 conquer한다.
요소들을 2묶음씩 반복적으로 merge한다.
'''

# 정렬되지 않은 데이터 입력
unsorted_list = [int(x) for x in input('data >> ').split()]

# 데이터가 한 개씩 남을 때까지 분할
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        # 데이터가 하나씩 남으면 리턴
        return unsorted_list
    # 절반으로 나눠주기
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    # 재귀를 이용하여 나눠진 것을 또 반으로 나눈다
    left1 = merge_sort(left)
    right1 = merge_sort(right)

    # 분할을 마쳤으면 merge로 넘어가기
    return merge(left1, right1)

def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[0]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

print(merge_sort(unsorted_list))