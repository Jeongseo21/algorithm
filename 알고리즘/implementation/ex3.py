'''
시뮬레이션
왕실의 나이트
'''

location = input('location >> ').split()
print(location)
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
count = 0
for key in data:
    if key == location[0]:
        location[0] = data[key]

steps = [(2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2), (-2, 1), (-2, -1)]

for step in steps:
    nx = int(location[0]) + int(step[0])
    ny = int(location[1]) + int(step[1])
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        count += 1

print(count)

'''
값을 입력받을 때
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
이런식으로 string의 인덱스를 활용해서 int형으로 바꿔고 시작해도 된다.
알파벳을 숫자로 바꿔야할 때 기억해두면 유용할 것 같다.
'''
