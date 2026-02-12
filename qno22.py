n = int(input("Enter the number"))
x = []
for i in range(0,n):
    y = input(f"Enter {i+1} string: ")
    x.append(y)

largest = ""
for j in range(0,n):
    if (len(x[j])>len(largest)):
        largest = x[j]
print(largest)
