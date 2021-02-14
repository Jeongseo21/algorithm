prioritis = [1, 2, 3]
location = 0

time = -1
result = 0

prio = []
for index, value in enumerate(prioritis):
    prio.append((value, index))
print(prio)

def maximum(prio):
    maxnum = 0
    for value, index in prio:
        if value > maxnum:
            maxnum = value
    return maxnum

while prio:
    now, index = prio.pop(0)
    if prio and now < maximum(prio):
        prio.append((now, index))

    else:
        result += 1
        if index == location:
            print(result)
