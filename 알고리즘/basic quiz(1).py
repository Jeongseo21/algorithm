# 다장조는 cdefgabC 총 8개 음으로 이루어져있다. 1,2,3,4,5,6,7,8fh 바꾸어 표현할 수 있다.
# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니면 mixed이다.
# 연주 순서가 주여졌을 때 무엇인지 판별하는 프로그램 만들어라

def haha(data):
    ascending = True
    descending = True

    for idx in range(len(data)-1):
        if data[idx] + 1 != data[idx+1]:
            ascending = False
        elif data[idx] - 1 != data[idx+1]:
            descending = False
    if ascending:
        print("acending")
    elif descending:
        print("descending")
    else:
        print("mixed")



data1 = [1,2,3,4,5,6,7,8]
data2 = [8,7,6,5,4,3,2,1]
data3 = [5,4,6,7,8,1,2,3]
haha(data1)
haha(data2)
haha(data3)

