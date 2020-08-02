#open hashing 기법
#충돌이 일어나면 링크드리스트로 추가적인 공간을 만드는 방법

hash_table= list(0 for i in range(8))

def data_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = data_key(data)
    hash_key = hash_function(index_key)

    if hash_table[hash_key] != 0:
        for index in range(len(hash_table[hash_key])):
            if hash_table[hash_key][index][0] == index_key:
                hash_table[hash_key][index][1] = value
                print(hash_table)
                return
            hash_table[hash_key].append([index_key, value])
            print(hash_table)
    else:
        hash_table[hash_key] = [[index_key, value]]
        print(hash_table)


def get_data(data):
    index_key = data_key(data)
    hash_key = hash_function(index_key)

    if hash_table[hash_key] != 0:
        for index in range(len(hash_table[hash_key])):
            if hash_table[hash_key][index][0] == index_key:
                return hash_table[hash_key][index][1]
        return None
    else:
        return None

print(hash_table)
save_data('Dave','Dave')
save_data('Dd', 'Dd')
save_data('han', 'haen')
save_data('im','bora')
save_data('han1', 'mongle')

print(get_data('han'))


