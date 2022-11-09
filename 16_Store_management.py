import csv

def Info():
    n = int(input("Enter total number of entries : "))
    x = []
    for i in range(n):
        EmpNo = int(input("Enter Employee Number : "))
        Name = input("Enter Name : ")
        Salary = int(input("Enter Salary : "))
        y = [EmpNo, Name, Salary]
        x.append(y)

    with open("Information.csv","w+") as f:
        writer = csv.writer(f)
        writer.writerow(["Employee Number","Name","Salary"])
        writer.writerows(x)
    f.close()

def search(t):
    with open("Information.csv","r") as g:
        b = next(g)
        temp = csv.reader(g)
        for i in temp:
            if len(i) == 0:
                a = i
            elif i[0] == t:
                print("Employee Number :",i[0],"Name :",i[1],"Salary :",i[2])
                break
        else:
            print("Error : No Employee Data exists for query.")

while True:
    print("MENU")
    print("Choice 1 : Add")
    print("Choice 2 : Search")
    print("Choice 3 : Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        Info()
    elif choice == 2:
        t = input("Enter Employee Number to search Employee details : ")
        search(t)
    elif choice == 3:
        quit()
    else:
        print("ERROR : Invalid Choice.")