n = int(input())

array = []
for i in range(n):
    # 공백을 기준으로 split
    input_data = input().split()
    # 이름은 문자열로, 점수는 정수로 변환해서 튜플에 저장
    array.append((input_data[0], int(input_data[1])))

# key를 이용해서 점수를 기준으로 정렬
sorted_array = sorted(array, key=lambda student: student[1], reverse=True)

print(sorted_array)
