# hash : 임의의 값을 고정 길이로 변환하는 것
# hash table : 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
# hashing function

hash_table = list(0 for i in range(5))
print(hash_table)

def hash_function(key):
    return key % 5

def storage_data(keyData,value):
    key = ord(keyData[0])
    hash_address = hash_function(key)
    hash_table[hash_address] = value

def get_data(keyData):
    key = ord(keyData[0])
    hash_address = hash_function(key)
    return hash_table[hash_address]



# print(ord(d1[0]),ord(d2[0]),ord(d3[0])) #키 값
# print(hash_function(ord(d1[0])),hash_function(ord(d2[0])),hash_function(ord(d3[0]))) #해시 주소

print(hash_table)

storage_data('dello', '00000')
storage_data('dye', '11111')
storage_data('haha', '22222')

print(hash_table)

print(get_data('bye'))



