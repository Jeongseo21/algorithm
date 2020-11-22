# 바닥 공사

n = int(input('n >> '))

d = [0] * 1001

#바텀업
d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]*2

print(d[n])