'''2) using the same data1 list(AS ABOVE)
    add few more elements to it till the user types the value as 1000 Or - 1000
    that time you STOP(NOTE 1000 or -1000 MUST NOT be added to the list, that is the EXIT point)

    sum all the positive number only which are 3 digits
    find the avg of those only which are 3 digits
    find the highest nummber, display it, then delete it
    THEN again find the highest number, display it - which number it displays?

    find the lowest number, display it, delete it
    AGAIN, find the lowest number, display it, delete it
    find the lowest number, display it - which number it displays?'''
three_digit_lst = []


while True:

    data1 = [78, 23, 199, 200, -66, -17, 50, 230, -
             992, 8, 0, 444, 55, -32, -49, 122, 440]

    loop = int(
        input('ENTER ANY NUMBER TO CONTINUE, ENTER 1000 OR -1000 TO STOP : '))

    if loop == 1000 or loop == -1000:

        break

    else:

        input_num = int(input('ENTER THE NUMBER : '))

        data1.append(input_num)

    for i in data1:

        if i > 0 and 100 <= i <= 999:

            three_digit_lst.append(i)


sum_num = sum(three_digit_lst)
avg_num = (sum_num/(len(three_digit_lst)))
max_num = max(three_digit_lst)
print()
print(three_digit_lst)
print()
print('THE SUM OF THREE DIGIT NUMBER IS : ', sum_num)
print('THE AVERAGE OF THREE DIGIT NUMBER IS : ', avg_num)
print('THE MAXIMUM OF THREE DIGIT NUMBER IS : ', max_num)
print()
print('------ AFTER DELETE THE THREE DEGIT MAXIMUM NUMBER ------')

three_digit_lst.remove(max_num)
print()
print(three_digit_lst)
print()
max_num = max(three_digit_lst)
print('THE MAXIMUM OF THREE DIGIT NUMBER IS : ', max_num)
min_num = min(three_digit_lst)
print()
print('THE MINIMUM OF THREE DIGIT NUMBER IS : ', min_num)
print()
print('------ AFTER DELETE THE THREE DEGIT MINIMUM NUMBER ------')
three_digit_lst.remove(min_num)
print()
print(three_digit_lst)
print()
min_num = min(three_digit_lst)
print()
print('THE MINIMUM OF THREE DIGIT NUMBER IS : ', min_num)
print()
print('------ AFTER DELETE THE THREE DEGIT MINIMUM NUMBER ------')
three_digit_lst.remove(min_num)
print()
print(three_digit_lst)
