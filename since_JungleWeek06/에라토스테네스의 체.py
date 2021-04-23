N = int(input())

def Eratos(N):
    nums = [False, False]+[True]*(N-1)
    primes = []

    for i in range(2, N+1):
        if nums[i]:
           primes.append(i)
           for j in range(i*2, N+1, i):
               nums[j] = False
        else:
            continue
    return primes

print(Eratos(N))