s_y = 1900  # default year
c_d = int(input('date:'))  # customer input date
c_m = int(input('month in number:'))  # customer input month
c_y = int(input('year:'))  # customer input year
if c_y >= s_y and 0000 <= c_y <= 9999:  # validation of date(dd-month-yyyy)
    if (c_m == 1 or c_m == 3 or c_m == 5 or c_m == 7 or c_m == 8 or c_m == 10 or c_m == 12):
        max1 = 31
    elif (c_m == 4 or c_m == 6 or c_m == 9 or c_m == 11):
        max1 = 30
    elif (c_y % 4 == 0 and c_y % 100 != 0 or c_y % 400 == 0):
        max1 = 29
    else:
        max1 = 28
    if (c_m < 1 or c_m > 12):
        print("Date is invalid.")
    elif (c_d < 1 or c_d > max1):
        print("Date is invalid.")
    else:
        l = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
        for i in range(1, 13):
            if i == c_m:
                c_m = l[i-1]

        d_y = c_y - s_y  # difference of year
        l_y = d_y//4  # leap year count
        sum = c_d + c_m + d_y + l_y
        week_day = sum % 7
        print(week_day)
