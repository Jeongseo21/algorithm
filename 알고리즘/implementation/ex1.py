'''
시뮬레이션 문제
- ex1. 상하좌우
'''

N = int(input("N >> "))
x, y = 1, 1
plan = input("plan >> ").split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
types = ['U', 'D', 'L', 'R']

for p in plan:
    for i in range(len(types)):
        if p == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<1 or nx>N or ny<1 or ny>N:
                continue
            else:
                x, y = nx, ny

print(x,y)