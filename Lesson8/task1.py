# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib
import random
import string

def sub_string_count(n):
    sub_string = {}
    letters = string.ascii_lowercase
    string_of_letters = ''.join(random.choice(letters) for i in range(n))
    print(string_of_letters)
    for leter in string_of_letters:
        hash_leter = hashlib.md5(leter.encode('utf-8')).hexdigest()
        print(hash_leter)
        if leter + '-' + hash_leter in sub_string:
            sub_string[leter + '-' + hash_leter] += 1
        else:
            sub_string[leter + '-' + hash_leter] = 1
    print(sub_string)


if __name__ == '__main__':
    sub_string_count(int(input('Enter length of string: ')))


