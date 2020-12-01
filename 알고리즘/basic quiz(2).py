# 블랙잭
# 카드의 합이 M을 넘지 않는 한도에서 카드의 합을 최대한 크게 만드는 게임

def blackjack(data, m):
    maxnum = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            for k in range(j+1, len(data)):
                sum = data[i] + data[j] + data[k]
                if  sum <= m:
                    maxnum = max(sum,maxnum)                
    print(maxnum)

data = [5,6,7,8,11]
m = 21
blackjack(data,m)