hash_table= list(0 for i in range(8))

def data_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    key = data_key(data)
    hash_key = hash_function(key)
    hash_table[hash_key] = value

def get_data(data):
    key = data_key(data)
    hash_key = hash_function(key)
    return hash_table[hash_key]

save_data('han','jeongseo')
save_data('oh', 'haen')
save_data('im','bora')

print(hash_table)

print(get_data('han'))
    