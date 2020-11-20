# 시간복잡도는 선택정렬과 똑같이 O(N^2)이지만
# 현재 데이터가 거의 정렬되어있을 때 매우 빠르게 동작한다.
# 최선의 경우 O(N)의 시간 복잡도를 가지며 거의 정렬되어있는 경우 퀵정렬보다도 빠르게 동작한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)