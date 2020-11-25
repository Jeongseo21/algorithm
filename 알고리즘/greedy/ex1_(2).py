coin = [100, 10, 500, 50]
N = 1850

count = 0
coin = sorted(coin, reverse=True)

for c in coin:

    if N == 0:
        break
    else:
        count += (N // c)
        # N을 c로 나눈 나머지, 1850 % 500 = 3...350
        N %= c
        '''
        N = N - (N // c) * c
        '''
print(count)




