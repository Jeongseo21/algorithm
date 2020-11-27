s = "1234" #사용자는 문자열로 입력

# s를 int형 리스트로 변환
s = [int(x) for x in s]

result = 0

for num in s:
    # 처음에 result가 0일 때 num으로 초기화
    if result == 0:
        result += num
    # num이 0이나 1일 때에는 더하기
    elif num == 0 or num == 1:
        result += num
    # 그 외의 수는 곱하기
    else:
        result *= num

print(result)