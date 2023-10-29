class RailFenceBasic:
    def Encryption(self, plain_text, depth):
        r = depth
        length = len(plain_text)
        c = length // depth
        mat = [['X' for _ in range(c)] for _ in range(r)]
        k = 0
        cipher_text = ""

        for i in range(c):
            for j in range(r):
                if k != length:
                    mat[j][i] = plain_text[k]
                    k += 1

        for i in range(r):
            for j in range(c):
                cipher_text += mat[i][j]

        return cipher_text

    def Decryption(self, cipher_text, depth):
        r = depth
        length = len(cipher_text)
        c = length // depth
        mat = [['X' for _ in range(c)] for _ in range(r)]
        k = 0
        plain_text = ""

        for i in range(r):
            for j in range(c):
                mat[i][j] = cipher_text[k]
                k += 1

        for i in range(c):
            for j in range(r):
                plain_text += mat[j][i]

        return plain_text


rf = RailFenceBasic()
depth = int(input("Enter depth for Encryption: "))
plain_text = input("Enter plain text: ")

cipher_text = rf.Encryption(plain_text, depth)
print("Encrypted text is:\n" + cipher_text)

decrypted_text = rf.Decryption(cipher_text, depth)
print("Decrypted text is:\n" + decrypted_text)