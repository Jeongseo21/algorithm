n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

reversed_array = sorted(array, reverse=True)

for num in reversed_array:
    print(num, end='  ')