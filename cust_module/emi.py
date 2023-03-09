loan_type = {'home loan': 17, 'personal loan': 14, 'education loan': 7.2, 'businees loan': 12,
             'vehicle loan': 9, 'gold loan': 14, 'agriculture loan': 6, 'wedding loan': 15, 'pool loan': 6}
cu_lo_type = str(input('enter what type of loan you want:'))
p = int(input('enter ammount required:'))
n = int(input('enter time period in month:'))
r = 0
for i in loan_type:
    if i == cu_lo_type:
        r += float(loan_type[i]/(12*100))


def emi(cu_lo_type, p, n):
    return p * r * ((1+r)**n)/((1+r)**n-1)


print(emi(cu_lo_type, p, n))
