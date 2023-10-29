from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class RSAEncryption:
    def __init__(self, key_size=1024):
        self.key = RSA.generate(key_size)
        self.private_key = self.key.export_key()
        self.public_key = self.key.publickey().export_key()

    def encrypt(self, plaintext):
        recipient_key = RSA.import_key(self.public_key)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        encrypted = cipher_rsa.encrypt(plaintext.encode())
        return encrypted

    def decrypt(self, ciphertext):
        private_key = RSA.import_key(self.private_key)
        cipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted = cipher_rsa.decrypt(ciphertext)
        return decrypted.decode()

rsa = RSAEncryption()

print("Enter the plain text:")
test_string = input()

print("Encrypting String:", test_string)
encrypted = rsa.encrypt(test_string)

print("Encrypted String in Bytes:", base64.b64encode(encrypted).decode())

decrypted = rsa.decrypt(encrypted)

print("Decrypted String in Bytes:", base64.b64encode(decrypted.encode()).decode())
print("Decrypted String:", decrypted)
