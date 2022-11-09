x = int(input("Enter total number of elements in your list : "))
i = 1
list1 = []
while i <= x:
    y = int(input("Enter element : "))
    list1.append(y)
    i += 1
list1.sort()
e = 0
for i in list1:
    if i > e:
        e = i
print("Largest Number : ",e)

for j in list1:
    if j < e:
        e = j
print("Smallest Number : ",e)