def armstrong(n):
    n = str(n)
    a = 0
    for i in n:
        i = int(i)
        i = i**3
        a = a + i
    n = int(n)
    if a == n:
        print("Number",n,"is an armstrong number.")
    else:
        print("Number",n,"is not an armstrong number")

n = int(input("Enter the number to check : "))
armstrong(n)
