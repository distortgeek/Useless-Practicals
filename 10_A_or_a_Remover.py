def aremover(file,newfile):
    y = ''
    z = ''
    with open(file, 'r',encoding="utf8") as f:
        x = f.read()
        for i in x:
            if i == "a" or i == "A":
                z = z + i
            else:
                y = y + i

    with open(newfile, 'w',encoding="utf8") as g:
        g.write(y)

    f.close()
    g.close()

file = input("Enter the file name : ")
newfile = input("Enter the new file name : ")
aremover(file,newfile)