'''The principle varies from 100000 to 200000 in steps of 10000 apply the rate of interest as 6.5 % pa time is 2 years
what is the Simple Interest and the Amount for each Principle amount display the Simple Interest and the amount.
SI = (P x T x R)/100
Amt = P + SI'''

rate = 6.5
time = 2


for principle in range(100000, 200000, 10000):
    simple_int = principle*rate*time/100
    amount = simple_int + principle
    print(simple_int, amount)
