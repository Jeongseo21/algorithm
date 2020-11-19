# 숫자 카드 게임
# 주어진 행 중에 한 개의 행을 선택하면 자동적으로 해당 행에서 가장 작은 숫자를 얻게 된다. 가장 큰 수를 얻도록 알고리즘을 짜로 얻은 수를 리턴해라
# 아이디어 : 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 것

# n은 행의 개수, m은 열의 개수
n, m = 2, 4
cards = [[7, 3, 1, 8], [3, 3, 3, 4]]

def cards_game(n, cards):
    min_cards = []

    for i in range(n):
        min_num = min(cards[i])
        min_cards.append(min_num)

    return max(min_cards)

print(cards_game(2, cards))

