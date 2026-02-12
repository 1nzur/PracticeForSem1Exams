values = ['A','A','A','A','A','B','B','B','C','C','D']
most_frequent = []
c = 1
check = {}
for i in values:
    if i in check:
        check[i] = check[i]+1
    else:
        check[i] = c
print(check)

max = 0
for key in check:
    if check[key]>max:
        max = check[key]
        most_frequent=key
print("Most frequent value = "+most_frequent)