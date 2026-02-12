def remove_at_idx():
    index = int(input("Enter the index you want to remove: "))
    if 0 <= index < len(list1):
        list1.pop(index)
        print("After removing:\n")
        for i in range(len(list1)):
            print(f"Index = {i}, Element = {list1[i]}\n")
    else:
        print("Invalid index!")

list1 = []
n = int(input("Enter the number of elements you want in your list: "))

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)

print("Before removing:\n")
for i in range(len(list1)):
    print(f"Index = {i}, Element = {list1[i]}\n")

remove_at_idx()