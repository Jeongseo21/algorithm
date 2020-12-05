N = int(input("N >> "))
stages = list(map(int, input("stages >> ").split()))
# 실패율을 저장할 리스트
failure = []
# 1부터 N까지 반복하면서 스테이지 도달한 경우 분모를 1 증가, 클리어한 경우 분자를 1 증가시킴
for i in range(1, N+1):
    deno, nume = 0, 0
    for stage in stages:
        # 도달하고 클리어한 경우, 분모 증가
        if stage >= i:
            deno += 1
        # 도달하기만 하고 클리어하지 못한 경우, 분자 증가
        if stage == i:
            nume += 1
    # 아무도 도달하지 못한 경우 실패율 0이므로 분모를 0에서 1로 증가(0/0은 division error)
    if deno == 0:
        deno = 1
    # 실패율 저장
    failure.append(nume/deno)

# 인덱스를 저장해줄 리스트 생성
index_list = []

for i in range(N):
    # 최대값 구해서 해당 인덱스+1을 리스트에 저장
    max_num = max(failure)
    index = failure.index(max_num)
    index_list.append(index+1)
    # 저장한 인덱스의 값은 -1로 변경
    failure[index] = -1

print(failure)
print(index_list)
