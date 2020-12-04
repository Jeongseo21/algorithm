'''
data = [['aaa', 20, 54, 75], ['bbb', 88, 64, 21], ['ccc', 55, 66, 45]]

korean = []
for i in range(len(data)):
    korean = sorted(data, key=lambda data, i: data[i][1])

print(korean)
'''
# 학생의 수 입력
N = int(input("N >> "))

# 학생의 이름과 점수 데이터 입력, 리스트 안에 튜플로 저장
data = []
for i in range(N):
    data.append(input("data >> ").split())

data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

print(data)
