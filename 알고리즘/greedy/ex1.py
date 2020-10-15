# 손님에게 거슬러줘야 할 돈이 n원일 때 거슬러줘야할 동전의 최소 개수를 구하시오 (500원, 100원, 50원, 10원 짜리 동전 사용)

def change(coin_list, price, pay):
    coin_list = [10, 50, 100, 500]
    coin_list.sort(reverse=True) #원본리스트를 역순정렬

    check_list = {}
    change = pay - price
    coin_count = 0

    for coin in coin_list:
        num = change // coin # 4700/500의 몫이 num에 저장
        change -= num * coin
        coin_count += num
        check_list[coin] = num
        print(check_list)

    return coin_count

print(change([10,50,100,500], 740, 2000))



