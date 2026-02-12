def vote(age):
    if age < 18:
        raise ValueError("not eligible: Must be 18 or older")
    else:
        print("Can vote")

try:
    test_age = int(input("Enter age: "))
    vote(test_age)
except ValueError as e:
    print(e)