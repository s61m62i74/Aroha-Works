'''create a new dictionary - by name , sal_purch
   move all the employees of Sales and Purchase into sal_purch , remove those employee from the emp
'''
emp = {100: ('Anand', 'Sales', 56400), 200: ('Vijay', 'Purchase', 67200), 333: ('Vani', 'Purchase', 37200), 220: ('Harish', 'Logistics', 32200),
       440: ('Vinay Vittal', 'Software', 75200), 289: ('Prakash Rao', 'Sales', 50000), 176: ('John Abraham', 'Software', 52000)}

sal_purch = {}
copy_emp = emp.copy()  # shallow copy
for key in emp:
    if 'Sales' in emp[key] or 'Purchase' in emp[key]:
        sal_purch[key] = emp[key]
        copy_emp.pop(key)
    else:
        continue
print("Sale Purchase Dictionary: ", sal_purch)
print("emp after reducing sales and purchase dept: ", copy_emp)
