def solution(a, b):
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    answer = ""
    day = 0
    for i in range(1, a+1):
        day += month[i-1]
    day += b

    if (day-1)%7 == 0:
        answer = "FRI"
    elif (day-1)%7 == 1:
        answer = "SAT"
    elif (day-1)%7 == 2:
        answer = "SUN"
    elif (day-1)%7 == 3:
        answer = "MON"
    elif (day-1)%7 == 4:
        answer = "TUE"
    elif (day-1)%7 == 5:
        answer = "WED"
    elif (day-1)%7 == 6:
        answer = "THU"
    return answer

print(solution(5,24))
