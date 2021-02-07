import sys

phone_book = ["119", "9767452", "119456"]
sorted()
for i in range(len(phone_book)):
    for j in range(i+1, len(phone_book)):
        if len(phone_book[i]) > len(phone_book[j]):
            continue
        print(phone_book[i], phone_book[j])
        if phone_book[i][::] == phone_book[j][:len(phone_book[i])]:
            return false
return true