s = "11001110101011100"

flag = False
count = 0
head = s[0]

for x in s:
    if flag == False:
        if x != head:
            flag = True
            count += 1
    else:
        if x == head:
            flag = False

print(count)
