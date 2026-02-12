x = input("Enter a string")
for i in x:
    if i in "@!$%^&*()_+-":
        x = x.replace(i,'#')
print(x)
