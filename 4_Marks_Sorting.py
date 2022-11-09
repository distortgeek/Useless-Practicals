n = int(input("Enter total number of students: "))

x = {}

for i in range(n):
    rno = int(input("Enter the roll number : "))
    name = input("Enter the name of student : ")
    marks = int(input("Enter the marks of student : "))

    x[rno] = [name, marks]

print("Result")
print(x)

for j in x:
    if x[j][1] > 75:
        print(x[j][0],"scored marks greater than 75.")
