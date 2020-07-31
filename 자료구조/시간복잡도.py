# 시간복잡도 : 알고리즘 실행 속도

#반복문이 기준이다.

#Big-O 표기법 : 최악의 실행 시간을 표기
#O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(2^n)<O(n!) #logn의 base는 2

#O(1) : 반복문이 없는 경우, n번 실행하는 경우

#O(n) : 반복문으로 인해 n번, n+10번, 3n+10번, 상수번 곱하겨나 상수번 더할 경우 이 상수는 시간 복잡도에 아무 영향도 미치지 못한다.

#O(n^2) : 이중for문으로 n n^2+1000, 3n^2+20

def sum_all(n):
    total = 0
    for num in range(1,n+1):
        total += num
    return total

print(sum_all(100)) #O(n)
print(sum_all(97))

def new_sum_all(n):
    return (1+n)*n/2

print(new_sum_all(97)) #O(1)
