'''
Q01_럭키 스트레이트
'''

# N을 입력받기
N = input("N >> ")
# N의 길이의 절반 구하기
half_len = len(N) // 2

# N을 숫자형 리스트로 변환
N = list(map(int, N))

# 왼쪽, 오른쪽 부분의 합 구하기
left = sum(N[:half_len])
right = sum(N[half_len:])

if left == right:
    print("LUCKY")
else:
    print("READY")


