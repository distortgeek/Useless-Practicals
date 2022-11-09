lst = []

def PushOn(Book):
    lst.append(Book)

def PopOut(Book):
    for i in lst:
        if Book == i:
            a = lst.index(i)
            lst.pop(a)

def Availability(Book):
    for i in lst:
        if Book == i:
            print("Book is available.")
        else:
            print("Book is not available.")

def Display():
    print("Books in Stack.")
    for i in lst:
        print(i)

while True: 
    print("Menu")
    print("Choice 1 : Add a Book.")
    print("Choice 2 : Remove a Book.")
    print("Choice 3 : Check Availability of a Book.")
    print("Choice 4 : Display Books in Stack.")
    print("Choice 5 : Exit")

    x = int(input("Enter your choice : "))

    if x == 1:
        Book = input("Enter book name : ")
        PushOn(Book)

    elif x == 2:
        Book = input("Enter book name : ")
        PopOut(Book)

    elif x == 3:
        Book = input("Enter book name : ")
        Availability(Book)

    elif x == 4:
        Display()

    elif x == 5:
        quit()

    else:
        print("Invalid choice")