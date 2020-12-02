'''
시뮬레이션
ex4)게임 개발
'''
# M, N 입력
M, N = map(int, input("M N >> ").split())

# x, y, direction 입력
x, y, direction = map(int, input('x y direction >> ').split())

# 방향을 움직이기 위한 dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# check로 방문한 노드 확인
check = [[0]*M for _ in range(N)]

# array로 육지 바다 맵 입력
array = []
for _ in range(N):
    array.append(list(map(int, input('>> ').split())))

# 움직인 칸의 수
count = 1
# 방향을 바꾼 횟수
turn_time = 0

# 왼쪽으로 방향을 바꾸는 함수, 북(0) 동(1) 남(2) 서(3)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션
# x, y 좌표 기준으로 turn_left한 nx,ny 구하기
while True:
    turn_left()
    # 왼쪽방향 좌표
    nx = x + dx[direction]
    ny = y + dy[direction]
    # nx, ny 좌표로 이동할 수 있으면 이동
    if check[nx][ny] == 0 and array[nx][ny] == 0:
        x, y = nx, ny
        check[nx][ny] = 1
        turn_time = 0
        count += 1
        continue
    else:
        turn_time += 1
    # 네 방향이 모두 이동 불가하면
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 이동
        if check[nx][ny] == 0 and array[nx][ny] == 0:
            x, y = nx, ny
            check[nx][ny] = 1
            turn_time = 0
            count += 1
        else:
            break

print(count)