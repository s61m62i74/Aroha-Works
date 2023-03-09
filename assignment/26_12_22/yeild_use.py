'''5) using this formala calc the YIELD TO Maturity(YTM)
    YTM=C + (FP - MP)/n
    - -----------------
    (FP + MP) / 2

    given
    C - coupoun payment Or also known as annual fixed interest
    FP - Face Value of the bond
    MP - Market Price of the bond
    n - numbers of years of maturity

    For example
    Assume that there is a bond on the market priced at Rs 850 and that the bond comes with a face value of RS 1, 000
    (a fairly common face value for bonds).
    On this bond, yearly coupons are Rs 150.
    The coupon rate for the bond is 15 % and the bond will reach maturity in 7 years.

    The YTM will be(after calc and applying the formula) is 18.53%'''


def calc_ytm(mp, fp, c, n):
    ytm = round(((c+(fp-mp)/n))/((fp+mp)/2)*100, 2)
    print()
    print('yeild to maturity is:', ytm, '%')


market_price = 850
face_value = 1000
coupon_payment = 150
no_of_yr = 7
calc_ytm(market_price, face_value, coupon_payment, no_of_yr)
