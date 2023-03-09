p = eval(input("enter the amount: "))
n = eval(input("enter the no of month:"))
type_of_loan = input("type of loan:")
sal = eval(input("enter curent sal:"))
exp = eval(input("enter the exp:"))
d = {'home loan': 17, 'personal loan': 14, 'education loan': 7.2, 'businees loan': 12,
     'vehicle loan': 9, 'gold loan': 14, 'agriculture loan': 6, 'wedding loan': 15, 'pool loan': 6}
r = 0
for i in d:
    if i == type_of_loan:
        r += float(d[i]/(12*100))  # rate per year


def emi(p, r, n):
    if 20000 <= sal <= 50000:
        max_s = sal+((100/100)*sal)
    elif 51000 <= sal <= 100000:
        max_s = sal+((65/100)*sal)
    else:
        return 'tou are not alegible'
    if 0 <= exp <= 1:
        max_e = sal + ((20/100)*sal)
    elif 1 <= exp <= 15:
        max_e = sal + ((80/100)*sal)
    elif 15 <= exp <= 30:
        max_e = sal + ((40/100)*sal)
    else:
        return 'you are not eligible'

    max_p = (max_s+max_e)/2
    if max_p <= p:
        return (p*r*(1+r)**n/((1+r)**n-1))


print(emi(p, r, n))
