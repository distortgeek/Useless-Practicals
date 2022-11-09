import csv

def IdandPass():
    n = int(input("Enter total number of entries : "))
    x = []
    for i in range(n):
        UserID = int(input("Enter user ID : "))
        Password = input("Enter password : ")
        y = [UserID, Password]
        x.append(y)

    with open("IDandPass.csv","a+") as f:
        writer = csv.writer(f)
        writer.writerow(["UserID","Password"])
        writer.writerows(x)
    f.close()

def search(t):
    with open("IDandPass.csv","r") as g:
        b = next(g)
        temp = csv.reader(g)
        for i in temp:
            if len(i) == 0:
                a = i
            elif i[0] == t:
                print("ID :",i[0],"Password :",i[1])
                break
        else:
            print("Error : Password not found.")

while True:
    print("MENU")
    print("Choice 1 : Add")
    print("Choice 2 : Search")
    print("Choice 3 : Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        IdandPass()
    elif choice == 2:
        t = input("Enter ID to search password : ")
        search(t)
    elif choice == 3:
        quit()
    else:
        print("ERROR : Invalid Choice.")