list1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}] 
dis = set()
for i in list1:
    for values in i.values():
        dis.add(values)
print(dis)