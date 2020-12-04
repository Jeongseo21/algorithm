data = [7, 5, 0, 9, 3]

for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
        else:
            break

print(data)

