with open("input.txt","r") as f1,open("output.txt","w") as f2:
    for lines in f1:
        cap = lines.upper()
        f2.write(cap)