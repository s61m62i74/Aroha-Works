'''data4 = (10,225.22,'12.2','55.22',-40,67,90,'191.22',4,-22,'-12.22',45,'12.10')
   process the above and ADD all the NON-NEGATIVE numbers and store them in a list
   sort the list
   display the TOP 2 highest value, 2 LEAST values.
'''
data4 = (10, 225.22, '12.2', '55.22', -40, 67, 90,
         '191.22', 4, -22, '-12.22', 45, '12.10')
data = list(data4)
l = []
for i in data:
    if type(i) in (int, float):
        if i >= 0:
            l.append(i)
l.sort()
print(l)
print('highest value:', l[-1])
print('2nd highest value:', l[-2])
print('least value:', l[0])
print('2nd least value:', l[1])
