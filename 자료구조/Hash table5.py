#hash table에서 충돌을 개선하는 기법

# 1.테이블의 저장공간을 확대하는 방법

#함수를 이용해서 문자열에 고유한 hash값을 주는 방법

# SHA-1, SHA-256 256이 더 보완되어 나온 함수임


import hashlib

str = 'STRING'
hash_object = hashlib.sha256() 
hash_object.update(str.encode()) #b'STRING'과 같음. 문자열을 바이트 형식으로 반환
hex_dig = hash_object.hexdigest()
print(hex_dig)

#해시테이블은 충돌이 없다면, O(1)이다.
#최악의 경우 모든 경우에 충돌이 발생한다면, O(n)이다.

#일반적인 경우 해시테이블의 시간복잡도는 O(1)이다.