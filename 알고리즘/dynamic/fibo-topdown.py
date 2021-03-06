'''
다이나믹 프로그래밍을 사용할 수 있는 조건
    조건1. 큰 문제를 작은 문제로 나눌 수 있다.
    조건2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일한 값을 가진다.
피보나치 수열을 위의 조건을 만족한다.

메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 한가지이다.
한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법이다.
캐싱이라고도 한다.
'''

# 한 번 계산된 결과를 메모이제이션하기 위해 리스트 초기화
d = [0]*100

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍 - 디버깅해보면 f(10)->f(9)->f(8) 순으로 진행된다.)
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1

    # 이미 계산한적이 있다면 메모되어있는 것 반환
    if d[x] != 0:
        return d[x]
    # 계산한적이 없다면 재귀함수로 계산
    else:
        d[x] = fibo(x-1) + fibo(x-2)
        return d[x]

print(fibo(10))
