import math
def sin(x,n):
    sin = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sin = sin + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    print(sin)


x=int(input("Enter the value of x :"))
n=int(input("Enter the length of series:"))
sin(x,n)