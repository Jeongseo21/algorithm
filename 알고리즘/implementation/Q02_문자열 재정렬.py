'''
string = input("string >> ")
# 문자형 숫자를 저장
num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

# array[0]에는 문자를, [1]에는 숫자를 입력
array = [[], []]

for s in string:
    if s in num:
        array[1].append(s)
    else:
        array[0].append(s)

# 문자를 정렬해준 후 join함수로 합침
array[0].sort()
array[0] = "".join(array[0])

# 숫자를 int형으로 바꿔서 더한 후 str형으로 다시 바꿈(join 함수로 문자와 합치기 위해서)
array[1] = str(sum(map(int,array[1])))

# 문자와 숫자를 합쳐서 출력
print("".join(array))
'''

data = input()
result = []
value = 0

for x in data:
    # 알파벳인 경우 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자인 경우 value에 더해주기
    else:
        value += int(x)

# 알파벳 오름차순으로 정렬
result.sort()

# 숫자가 존재하는 경우 뒤에 삽입
if value != 0:
    result.append(str(value))

print("".join(result))

