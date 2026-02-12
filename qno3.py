def add():
    result = a+b
    return result

def sub():
    result = a-b
    return result

def multi():
    result = a*b 
    return result

def div():
    result = a/b 
    return result

while True:
    op = int(input("\nSelect the option you want to do \n1 to add \n2 to substract \n3 to multiply \n4 to divide \n5 to exit: "))
    if(op==5):
        break
    else:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if(op==1):
            print(add())
        elif(op==2):
            print(sub())
        elif(op==3):
            print(multi())
        elif(op==4):
            print(div())
