numbers = [2, 20, 200]
str_numbers = list(map(str, numbers))

answer = ''
to_sort = []

for snum in str_numbers:
    if len(snum) < 4:
        new = (snum *4)[:4]
    else:
        new = '1000'
    to_sort.append((new, snum))

to_sort.sort(reverse=True)

for new, origin in to_sort:
    answer += origin
if int(answer) == 0:
    print('0')
else:
    print(answer)


## idea ) 모든 수를 네 자리 수로 만든다.

