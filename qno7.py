c = 0
with open("story.txt","r") as f1:
    for lines in f1:
        c = c+1
print('total lines = ',c)