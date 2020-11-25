N, M = map(int, input("N M >> ").split())
count = 0

while N != 1:
    if N % M == 0:
        N //= M
        count += 1
    else:
        N -= 1
        count += 1

print(count)
