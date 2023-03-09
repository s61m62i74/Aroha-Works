'''data2 = [12,54,31,66,155,89,22,29,39,100,125,500]
   data3 = (122,155,49,29,31)
   process the data2 ADD all the members of data3 to data2
   the resultant list generated from above - convert it into set - to remove duplicate elements
   SORT the set - display in DESC order
'''
data2 = [12, 54, 31, 66, 155, 89, 22, 29, 39, 100, 125, 500]
data3 = (122, 155, 49, 29, 31)

data2.extend(list(data3))
print(data2)
set_data = set(data2)
print(set_data)

print(sorted(set_data, reverse=True))
