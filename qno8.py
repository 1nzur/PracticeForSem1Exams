with open("numbers.txt","r") as f1,open("square.txt","w") as f2:
    for numbers in f1:
        x = int(numbers)*int(numbers)
        f2.write(str(x))
        f2.write("\n")