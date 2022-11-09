def sorter(file):
    lchar = uchar = vow = const = num = splchar = 0
    with open(file, 'r',encoding='utf-8') as f:
        x = f.read()
        for i in x:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                vow = vow + 1
                if i.isupper():
                    uchar = uchar + 1
                else:
                    lchar = lchar + 1
            elif i != "aeiouAEIOU":
                const = const + 1
                if i.isupper():
                    uchar = uchar + 1
                else:
                    lchar = lchar + 1
            elif type(i) == 'int':
                num = num + 1
            else:
                splchar = splchar + 1

    f.close()
    print("There are",uchar, "uppercase characters in file.")
    print("There are",lchar, "lowercase characters in file.")
    print("There are",vow,"vowels in file.")
    print("There are",const,"constants in file.")
    print("There are",num,"numbers in file.")
    print("There are",splchar, "special characters in file")


file = input("Enter file name : ")
sorter(file)