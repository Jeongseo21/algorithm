# 1일 될 때 까지
# 최대한 많이 나누는 것이 최적해를 보장한다.

n, k = 25, 3
count = 0

while n != 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
print(count)

