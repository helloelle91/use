text = input("Enter text : ")
row = int(input("Enter number of rows : "))
col = int(input("Enter number of columns : "))
cipher = ""
cipher1 = ""
choice = []
mat = []
mat1 = []
size = row*col
if len(text) > size:
    print("The length of text entered exceeds the size of the matrix")
    print("Please increase the size")

if len(text) < size:
    for i in range(0, size - len(text)):
        text+=" "
        
if len(text) == size:        
    for i in range (0,row):
        mat.append([])
        mat1.append([])  
        c = int(input(f"Enter the new position for row {i+1} : "))
        choice.append(c) 
        for j in range(i,len(text),row):
            mat[i].append(text[j]) 

    for i in range(0,row):
        mat1[i] = mat[choice[i]]
    for i in range(0,row):
        for j in range(0,col):
            cipher += mat1[i][j]   

    print("Encrypted text : ", cipher)

    for i in range(0,row):
        mat[choice[i]] = mat1[i]
    for i in range(0,col):
        for j in range(0,row):
            cipher1 += mat[j][i]

    print("Decrypted text : ", cipher1)