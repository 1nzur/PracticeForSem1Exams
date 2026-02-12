def is_palindrome(dna):
    dna = dna.lower()
    return(dna == dna[::-1])

d = input("Enter the dna structure")
print(is_palindrome(d))
