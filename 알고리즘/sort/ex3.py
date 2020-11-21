a_array = [1, 2, 5, 4, 3]
b_array = [5, 9, 7, 6, 5]
k = int(input('k>>'))
'''
# 1차 접근

for i in range(k):
    a_min = min(a_array)
    b_max = max(b_array)
    if a_min < b_max:
        a_array.remove(a_min)
        a_array.append(b_max)
        b_array.remove(b_max)
        b_array.append(a_min)
'''

a_array.sort()
b_array.sort(reverse=True)

for i in range(k):
    if a_array[i]<b_array[i]:
        a_array[i], b_array[i] = b_array[i], a_array[i]
    else:
        break

print(sum(a_array))



