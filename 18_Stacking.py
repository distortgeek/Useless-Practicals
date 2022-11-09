def tpush():
    n = int(input("Enter total number of entries: "))
    R = {} 
    for j in range(n):
        name = input("Enter the name of student : ")
        marks = int(input("Enter the marks of student : "))
        R[name] = marks
    def test(R):
        global lst
        lst = []
        for i in R:
            if int(R[i]) > 75:
                lst.append(i)
        print(lst)
    test(R)

def tpop(u):
    lst.pop(u)
    print(lst)

def tdisplay():
    for i in lst:
        print(i)

while True: 
    print("Menu")
    print("Choice 1 : Push Elements in stack from a Dictionary.")
    print("Choice 2 : Pop Elements from Stack(One at a time).")
    print("Choice 3 : Display Elements in Stack.")
    print("Choice 4 : Exit")

    x = int(input("Enter your choice : "))

    if x == 1:
        tpush()

    elif x == 2:
        u = int(input("Enter the position of name to remove : "))
        tpop(u)

    elif x == 3:
        tdisplay()

    elif x == 4:
        quit()

    else:
        print("Invalid choice")