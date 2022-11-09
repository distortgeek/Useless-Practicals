print("Program to find roots of a quadratic equation.")
a = float(input("Enter 1st coefficient of equation(a) : "))
b = float(input("Enter 2nd coefficient of equation(b) : "))
c = float(input("Enter 3rd coefficient of equation(c) : "))
d = (b**2) - (4*a*c)
print("Deteminant of equation :",d)
if d > 0 or d < 0:
    d = d**(1/2)
    x1 = ((-b + d) / (2*a))  
    x2 = ((-b - d) / (2*a))  
    print("Coefficients of equation : ",x1,"and",x2)
else:
    x = (-b/(2*a))
    print("Coefficients of equation : ",x)