p = int(input("Enter the Modulo(p): "))
root = int(input("Enter the Primitive Root(a): "))
Xa = int(input("Enter the secret key(X): "))
Xb = int(input("Enter the secret key(Y): "))

Ya = (root**Xa)%p
Yb = (root**Xb)%p
print("Ya = ", Ya)
print("Yb = ", Yb)

S_A = (Yb**Xa)%p
S_B = (Ya**Xb)%p
print("S_A = ", S_A)
print("S_B = ", S_B)


if S_A == S_B:
    print("Transmission Successful")
else:
    print("Transmission Failed")