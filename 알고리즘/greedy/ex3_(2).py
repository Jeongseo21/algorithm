N, M = map(int, input("N M >> ").split())

cards_list = []

for i in range(N):
    cards = list(map(int, input(f"cards {i}행 >> ").split()))
    cards_list.append(cards)

min_num = 0
for cards in cards_list:
    if min_num < min(cards):
        min_num = min(cards)

print(min_num)
