import pickle

x = {}

def addstudent():
    with open("Record.dat","ab+") as f:
        n = int(input("Enter total number of entries : "))
        for i in range(n):
            roll = int(input("Roll Number : "))
            name = input("Student Name : ")
            x[name] = roll
        pickle.dump(x,f)

def search(roll):
    with open ('Record.dat','rb') as f:
        temp=pickle.load(f)
        for j in temp:
            if temp[j] == roll:
                print("Roll Number:",temp[j])
                print("Name:",j)
                break
        else:
            print("ERROR : NOT FOUND")

while True:
    print("MENU")
    print("Choice 1 : Add")
    print("Choice 2 : Search")
    print("Choice 3 : Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        addstudent()
    elif choice == 2:
        t = int(input("Enter roll number : "))
        search(t)
    elif choice == 3:
        quit()
    else:
        print("ERROR : Invalid Choice.")