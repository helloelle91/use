import random

def encrypt(pt, key):
    et = []
    for i in range(len(pt)):
        a = ord(pt[i]) - ord('a')
        b = ord(key[i]) - ord('a')
        c = (a + b) % 26
        et.append(chr(c + ord('a')))
    return ''.join(et)

def generate_key(n):
    a = ord('a')
    z = ord('z')
    strlen = n
    random.seed()
    key = ''.join(chr(random.randint(a, z)) for i in range(strlen))
    return key


print("Enter Plain Text:")
pt = input()
strlen = len(pt)

print("Keyword:")
keyword = generate_key(strlen)
print(keyword)

print("Encrypted Text:")
et = encrypt(pt, keyword)
print(et)

