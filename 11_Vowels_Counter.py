def vowcounter(file):
    a = e = i = o = u = A = E = I = O = U = 0 
    with open(file, 'r',encoding="utf8") as f:
        x = f.read()
        for j in x:
            if j == 'a':
                a = a + 1
            elif j == 'e':
                e = e + 1
            elif j == 'i':
                i = i + 1
            elif j == 'o':
                o = o + 1
            elif j == 'u':
                u = u + 1
            elif j == 'A':
                A = A + 1
            elif j == 'E':
                E = E + 1
            elif j == 'I':
                I = I + 1
            elif j == 'O':
                O = O + 1
            elif j == 'U':
                U = U + 1
    f.close()

    print("Count of a : ",a)
    print("Count of e : ",e)
    print("Count of i : ",i)
    print("Count of o : ",o)
    print("Count of u : ",u)
    print("Count of A : ",A)
    print("Count of E : ",E)
    print("Count of I : ",I)
    print("Count of O : ",O)
    print("Count of U : ",U)

file = input("Enter the file name: ")
vowcounter(file)