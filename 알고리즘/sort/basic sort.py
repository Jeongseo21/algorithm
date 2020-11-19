# 2020.08.18
# 버블정렬, 선택정렬, 삽입정렬 강의자료만 보고 구현하기

# 버블정렬 O(n^2)
# 완전정렬이 되어있는 경우(최선의 경우) O(n)

def bubbleSort(data_list):
    for num in range(len(data_list)-1):
        swap = 0
        for idx in range(len(data_list)-num-1):
            if data_list[idx]>data_list[idx+1]:
                data_list[idx], data_list[idx+1] = data_list[idx+1], data_list[idx]
                swap += 1
        if swap == 0:
            break
    return data_list

data_list = [7,6,5,4,3,2,1]
print(bubbleSort(data_list))


# 선택정렬 O(n^2)
def selectionSort(data_list):
    for num in range(len(data_list)):
        lowest = num
        swap = 0
        for idx in range(num+1, len(data_list)):
            if data_list[lowest] > data_list[idx]:
                lowest = idx
                swap += 1
        data_list[num], data_list[lowest] = data_list[lowest], data_list[num]

        if swap == 0:
            break
    return data_list

data_list = [7,6,5,4,3,2,1]
print(selectionSort(data_list))


# 삽입정렬 O(n^2)
def insertionSort(data_list):
    for num in range(1, len(data_list)):
        for idx in range(num, 0, -1):
            if data_list[idx-1] > data_list[idx]:
                data_list[idx], data_list[idx-1] = data_list[idx-1], data_list[idx]

    return data_list

data_list = [7,6,5,4,3,2,1]
print(insertionSort(data_list))