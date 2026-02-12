data = ['A','A','A','A','A','B','B','B','C','C','D']
def search():
    count = 0
    x = input("Enter the data you want to search")
    for i in data:
        if x==i:
            count = count+1
    if count == 0:
        print("Data not in datalist")
    else:
        print(x,"is repeated",count,"times")
search()