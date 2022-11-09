def hashseprator(file,newfile):
    a = ''
    with open(file, 'r',encoding="utf8") as f:
        x = f.read()
        for i in x:
            if i == "  ":
                a = a + "##"
            elif i == " ":
                a = a + "#"
            else:
                a = a + i + "#"

    with open(newfile, 'w',encoding="utf8") as g:
        g.write(a)

    f.close()
    g.close()

file = input("Enter the file name : ")
newfile = input("Enter the new file name : ")
hashseprator(file,newfile)