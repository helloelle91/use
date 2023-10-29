def affine_cipher(message, a, b):
    cipher_text = ""
    for char in message:
        cipher_text += chr((a * ord(char) + b) % 26 + ord('A'))
    print(cipher_text)

affine_cipher("Hello World", 5, 8)