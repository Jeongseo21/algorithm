import sys

M = int(input())

result_set = 0

for _ in range(M):
    a = input().split()

    if a[0] == "all":
        result_set = (1<<21)-1
        # print(bin(result_set))
        continue
    elif a[0] == "empty":
        result_set = 0
        continue

    num = int(a[1])

    if a[0] == "add":
        result_set |= 2**num
        continue
        # print(bin(result_set))
    if a[0] == "check":
        if result_set & 2**num == 0:
            print(0)
            continue
        else:
            print(1)
            continue
    if a[0] == "remove":
        result_set -= (1<<num)
        continue
        # print(bin(result_set))
    if a[0] == "toggle":
        if result_set & 2**num == 0:
            result_set |= 2**num
            continue
            # print(bin(result_set))
        else:
            result_set -= (1<<num)
            continue
            # print(bin(result_set))
