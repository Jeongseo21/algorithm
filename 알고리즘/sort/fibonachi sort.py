# 2020.08.20
# 피보나치 수열

# 재귀함수(recursive call)로 구현
def recallFibo(num):
    if num <= 1:
        return num
    else:
        return recallFibo(num-1)+recallFibo(num-2)

print(recallFibo(0))
print(recallFibo(1))
print(recallFibo(2))
print(recallFibo(3))
print(recallFibo(4))
print(recallFibo(5))
print(recallFibo(6))
print(recallFibo(7))

# 동적계획법(dynamic programming)으로 구현
def dynamicFibo(num):
    fibo_list = [ 0 for i in range(num+1) ]
    fibo_list[0] = 0
    fibo_list[1] = 1
    for idx in range(2, num+1):
        fibo_list[idx] = fibo_list[idx-1] + fibo_list[idx-2]
    return fibo_list[num]


print(dynamicFibo(3))
print(dynamicFibo(4))
print(dynamicFibo(5))
print(dynamicFibo(6))
print(dynamicFibo(7))