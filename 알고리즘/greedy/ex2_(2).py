num = [2, 4, 5, 4, 6]
M = 8
K = 3

num.sort()
print(num)
a, b = num[-1], num[-2]

answer = (M // (K + 1)) * (a * K + b) + (M % (K + 1)) * a

print(answer)