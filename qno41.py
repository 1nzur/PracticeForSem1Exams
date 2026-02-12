dic1 = {'a':1,'b':2,'c':3}
x = input("enter a string")
for i in dic1:
    if x in dic1.keys():
        print("it is already in dictionary")
        break
    else:
        print("It is not in dictionary")
        break
