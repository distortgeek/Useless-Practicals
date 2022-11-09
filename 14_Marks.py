# import pickle

# def addstudent():
#     x = {}
#     with open("Record.dat","ab+") as f:
#         n = int(input("Enter total number of entries : "))
#         for i in range(n):
#             roll = int(input("Roll Number : "))
#             name = input("Student Name : ")
#             marks = int(input("Marks : "))
#             x[name] = [roll,marks]
#             pickle.dump(x,f)

# def update(roll,marks):
#     with open ('Record.dat','rb+') as f:
#         temp=pickle.load(f)
#         for j in temp:
#             if temp[j][0] == roll:
#                 temp[j][1] = marks
#                 pickle.dump(temp,f)
#                 print("Successfully Updated Marks.")
#                 break
#         else:
#             print("ERROR Occurred.")

# def display():
#         with open ('Record.dat','rb+') as f:
#             while True:
#                 temp=pickle.load(f)
#                 print(temp)
#             for j in temp:
#                 print("Roll Number : ",temp[j][0])
#                 print("Name : ",j)
#                 print("Marks : ",temp[j][1])

# while True:
#     print("MENU")
#     print("Choice 1 : Add")
#     print("Choice 2 : Update")
#     print("Choice 3 : Display")
#     print("Choice 4 : Exit")

#     choice = int(input("Enter Choice : "))

#     if choice == 1:
#         addstudent()
#     elif choice == 2:
#         t = int(input("Enter roll number : "))
#         g = int(input("Enter marks to update : "))
#         update(t,g)
#     elif choice == 3:
#         display()
#     elif choice == 4:
#         quit()
#     else:
#         print("ERROR : Invalid Choice.")