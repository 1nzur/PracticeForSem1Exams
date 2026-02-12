
my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}
def get_value(item):
    return item[1]
asc_sorted = dict(sorted(my_dict.items(), key=get_value))
print("Ascending:", asc_sorted)

dsc_sorted = dict(sorted(my_dict.items(),key=get_value,reverse=True))
print("Decending:",dsc_sorted)