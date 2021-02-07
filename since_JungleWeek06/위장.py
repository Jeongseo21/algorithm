import sys
from itertools import combinations
category = set()

clothes = [["a", "a"], ["b", "b"], ["c", "c"]]

for cloth in clothes:
    category.add(cloth[-1])
category = list(category)

result = [0 ] *len(category)

for i in range(len(category)):
    for cloth in clothes:
        if cloth[-1] == category[i]:
            result[i] += 1


print(result)
total = 1
for i in range(len(result)):
    total *= result[i] + 1
print(total -1)

# total = 0
# for i in range(1, len(result)+1):
#     combi = list(combinations(result, i))
#     for case in combi:
#         cases.append(list(case))
#
# print(cases)
#
# for case in cases:
#     if len(case) == 1:
#         total += case[0]
#         continue
#     tmp = 1
#     for i in range(len(case)):
#         tmp *= case[i]
#     total += tmp


