participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

flag = [True] * len(participant)

for val in completion:
    for i, v in enumerate(flag):
        if v and participant[i] == val:
            flag[i] = False
            break

print(flag)
for i, v in enumerate(flag):
    if v:
        print(participant[i])


