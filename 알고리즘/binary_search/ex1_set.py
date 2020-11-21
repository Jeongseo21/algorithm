# 부품탐색 - set()을 사용한 방법

N = int(input('N >> '))
N_array = list(map(int, input('N_array >> ').split()))
M = int(input('M >> '))
M_array = list(map(int, input('M_array >> ').split())) # 중복을 제거해야한다면 set()을 사용해도됨

def search(N, M, N_array, M_array):
    for m in M_array:
        if m in N_array:
            print('yes', end=' ')
        else:
            print('no', end=' ')

search(N, M, N_array, M_array)