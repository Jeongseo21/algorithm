from itertools import chain, combinations

coins = [3, 2, 1, 1, 9]
money = []

# coins의 부분집합 구하기
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

cases = list(powerset(coins))

# 부분집합의 합을 구한 후 money에 중복 제외하고 저장
for case in cases:
    total = 0
    for c in case:
        total += c
    if total not in money:
        money.append(total)

# 1부터 money에 들어있는지 확인, 없으면 출력
for i in range(len(money)):
    if i not in money:
        print(i)
        break