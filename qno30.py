data = ['A','A','A','A','A','B','B','B','C','C','D']
freq = {}
for i in data:
    if i in freq:
        freq[i] = freq[i]+1
    else:
        freq[i] = 1
for i in freq:
    print(str(freq))
