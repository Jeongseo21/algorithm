brown = 10
yellow = 2

# brown이 가능한 경우의 수를 모두 구함
cnddt_brown = []

for col in range(5000+1):
    for row in range(col, 5000+1):
        if brown == col * row - ((col-2) * (row-2)):
            cnddt_brown.append((col, row))

for col, row in cnddt_brown:
    if yellow == (col-2)*(row-2):
        print([row, col])