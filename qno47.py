list1 = [1,2,3,4,5,6,7,2,2,3,4,5,6,1,1,1,1,1]
x = int(input("Enter the potential element: "))
c=0
if x not in list1:
    print("Element not in list")
else:
    for i in list1:
        if x == i:
            c = c+1
print(f"the element {x} is repeated {c} times")