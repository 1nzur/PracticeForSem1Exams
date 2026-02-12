x = "The quick Brown Fox"
cap = 0
low = 0
for i in x.strip():
    if i.isupper():
        cap = cap+1
    else:
        low = low+1
print(cap)
print(low)