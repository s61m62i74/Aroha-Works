# Given the mileage of a vehicle is 12km/liter of Petrol and  15.5 /km/liter if the fuel is Deisel
# Also Given the rate of 1 liter of Petrol is Rs 101.95 rate of 1 liter of Deisel is Rs 87.85
# Keep inputting the data till the user type NEGATIVE number to QUIT out ask the user the type of vehicle ask the user how many kilometer is the trip calculate the amount of fuel needed and the price of it.
#   ....
#    Example
#       Enter 1 for Petrol, 2 for Deisel type of vehicle:  1
#        Enter the journey to cover in Km:   300

#         just showing..... 300/12  will give  total Petrol need in liter say T
#         T x 101.95 = will give the trip expense.
#     NOTE:: if the user inputs anything apart from 1 , 2 OR negative number then JUST IGNORE it ....
#     this HINT is good enough...
while True:
    entry = int(
        input('enter 1 for petrol or 2 for diesel or any other number to quit:'))
    if entry == 1 or entry == 2:
        km = int(input('enter the total distance:'))
    if entry == 1:
        petrol_rqrd = km/12
        trip_xpnce = petrol_rqrd*101.95
        print(trip_xpnce)
    elif entry == 2:
        diesel_rqrd = km / 15.5
        trip_xpnce = diesel_rqrd * 87.85
        print(trip_xpnce)
    else:
        break
