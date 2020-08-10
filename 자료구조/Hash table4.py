#Linear Probing 기법, 폐쇄해싱 또는 Close Hashing 기법 중 하나.
#저장 공간 활용도가 높아짐

import hashlib

hash_table= list(0 for i in range(8))

def data_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = data_key(data)
    hash_key = hash_function(index_key)
    print(hash_key)

    if hash_table[hash_key] != 0:
        for index in range(hash_key, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key,value]
                print(hash_table)
                return
            elif hash_table[index][0] == index_key:
                hash_table[index] = [index_key,value]
                print(hash_table)
                return
    else:
        hash_table[hash_key] = [index_key, value]
        print(hash_table)


def get_data(data):
    index_key = data_key(data)
    hash_key = hash_function(index_key)

    if hash_table[hash_key] != 0:
        for index in range(hash_key, len(hash_table)):
            if hash_table[index][0] == index_key:
                return hash_table[index][1]
        return None
    else:
        return None

print(hash_table)
save_data('Dave','Dave')
save_data('Dd', 'Dd')
save_data('han', 'haen')
save_data('im','bora')
save_data('han1', 'mongle')

print(get_data('han1'))
