# 1. pivot을 선택한다
# 2. pivot을 기준으로 비교데이터가 작으면 왼쪽, 크면 오른쪽에 배치한다.
# 3. 재귀적으로 정렬한다.

# O(nlog(n)) - 빅오표기법은 최악의 시간을 가정하는 것. 
# 하지만 이 경우는 평균적인 시간복잡도를 쓴다.
# 피봇 양쪾으로 n/2씩 나눠진다고 가정하면 
# nlogn의 시간복잡도를 가진다.
# 최악의 경우, 피봇이 한쪽으로 완전 치우쳐있을 때는 O(n^2)이 걸리지만 흔치않은 경우이다.
# 일반적으로 병합정렬보다 빠르다.
import random

def quick_sort(data):
    if len(data) <= 1:
        return data
    left, right = list(), list()
    pivot = data[0]
    for idx in range(1, len(data)):
        if data[idx]<pivot:
            left.append(data[idx])
        else:
            right.append(data[idx])
    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_conph(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item >= pivot]
    
    return quick_conph(left) + [pivot] + quick_conph(right)

data = random.sample(range(100),10)
print(quick_sort(data))
print(quick_conph(data))
