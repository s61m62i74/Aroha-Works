'''using the emp 
   find out the max salary, min salary , avg salary of ALL the employee
   avg salary paid to the employees working in Sales dept.
'''
emp = {100: ('Anand', 'Sales', 56400), 200: ('Vijay', 'Purchase', 67200), 333: ('Vani', 'Purchase', 37200), 220: ('Harish', 'Logistics',
                                                                                                                  32200), 440: ('Vinay Vittal', 'Software', 75200), 289: ('Prakash Rao', 'Sales', 50000), 176: ('John Abraham', 'Software', 52000)}

sal = []
li = list(emp.values())
for i in li:
    for j in i:
        sal += [i[2]]

max_salary = max(sal)
print('maximum salary:', max_salary)
min_salary = min(sal)
print('minimum salary:', min_salary)
avg_salary = sum(sal)/len(sal)
print('avrage salary:', avg_salary)
sales_sal_list = []
for key in emp:
    for sal in emp[key]:
        if emp[key][1] == 'Sales':
            sales_sal_list.append(emp[key][-1])
            break
sales_sal_avg = sum(sales_sal_list)/len(sales_sal_list)
print('Average salary of sales department is:', sales_sal_avg)
