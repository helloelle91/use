#Caesar Cipher

def encrypt(str, shift):
    cipher_text = ""
    for char in str:
        cipher_text += chr(((ord(char) + shift - 97) % 26) + 97)
    return cipher_text

def decrypt(str, shift):
    plain_text = ""
    for char in str:
        plain_text += chr(((ord(char) - shift - 97) % 26) + 97)
    return plain_text 

plain_text = "Hello".lower()
shift = 3
result1 = encrypt(plain_text, shift)
result2 = decrypt(result1, shift)
print("Cipher text: ", result1)
print("Plain text: ", result2)
