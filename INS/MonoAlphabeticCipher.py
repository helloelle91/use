def shift_message(message, shift):
    return alphabet[(alphabet.index(message)+ shift) % len(alphabet)]

def encrypt(text, amt):
    cipher_text = ""
    for i in text:
        if i in alphabet:
            cipher_text += shift_message(i, amt)
        else:
            cipher_text += i
    return cipher_text

def decrypt(text, amt):
    plain_text = ""
    for i in text:
        if i in alphabet:
            plain_text += shift_message(i, -amt)
        else:
            plain_text += i    
    return plain_text

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
plain_text = "Hello@123"
shift = 3
result1 = encrypt(plain_text, shift)
result2 = decrypt(result1, shift)
print("Cipher text: ", result1)
print("Plain text: ", result2)
