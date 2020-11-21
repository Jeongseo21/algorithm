# 부품탐색 - 계수 정렬을 사용한 방법

N = int(input('N >> '))
N_array = list(map(int, input('N_array >> ').split()))
M = int(input('M >> '))
M_array = list(map(int, input('M_array >> ').split())) # 중복을 제거해야한다면 set()을 사용해도됨

count = [0]*1000000 # 계수 정렬은 공간효율성이 좋지 않다.

# 부품번호를 인덱스로 두고 부품이 있으면 1
for n in N_array:
    count[n] = 1

# 손님이 요청한 부품이 있나 확인
for m in M_array:
    if count[m] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


