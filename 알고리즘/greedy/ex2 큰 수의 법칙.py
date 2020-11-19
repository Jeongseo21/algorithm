# 큰 수의 법칙
# 아이디어 : 입력값 중에 가장 큰 수와 두 번째로 큰 수만 저장해서, 가장 큰 수를 k번 더하고 두 번째로 큰 수를 한 번 더하는 연산을 반복하면 된다


# 최대숫자 구하기
def the_biggest(m, k, nums):
    # nums를 정렬해서 가장 큰 수와 두 번째로 큰 수를 저장
    nums.sort()
    max_num = nums[-1]
    second_num = nums[-2]


    # 결과값을 저장할 total, 조건문의 기준이 되는 count 변수 선언
    total = 0
    count = True

    # m이 0이 될때까지 반복
    while m:
        #count가 True면 max_num * k를 더하기
        if count:
            total += max_num * k
            count = False
            m -= k
        #count가 False면 second를 한 번 더하기
        if not count:
            total += second_num
            count = True
            m -= 1

    return total


n, m, k = 5, 8, 3

nums = [2, 4, 5, 4, 6]

print(the_biggest(m, k, nums))

