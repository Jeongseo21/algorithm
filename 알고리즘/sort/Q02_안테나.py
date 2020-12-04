'''
# 집의 개수 입력
house_n = int(input("N >> "))

# 집의 위치 입력
houses = [int(x) for x in input('집의 위치 >> ').split()]

# 집의 위치에서 가장 큰 값이 점의 개수
N = max(houses)

# results에 안테나의 위치에 따른 집까지의 거리의 합을 저장
results = []
# 1부터 N까지 반복, 안테나의 위치
for i in range(1, N+1):
    # vlaue 0으로 초기화
    value = 0
    # 집의 위치를 하나씩 가져와서 안테나와의 거리(distance) 저장
    for house in houses:
        distance = house - i
        # 거리가 음수면 양수로 바꿈
        if distance < 0:
            distance = -distance
        # 거리의 합을 value에 저장
        value += distance
    # 각각의 거리의 합을 result에 저장, (result의 인덱스 값 + 1)이 실제 집의 위치
    results.append(value)

# 저장된 거리 중 최소값 저장
min_num = min(results)

# enumerate를 사용해서 최소값의 인덱스 반환
for i, d in enumerate(results):
    if d == min_num:
        print(i+1)
        break
'''
n = int(input("n >> "))
data = list(map(int, input().split()))
data.sort()

# 중간값 출력
print(data[(n-1)//2])