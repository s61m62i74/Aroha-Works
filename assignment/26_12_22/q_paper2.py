'''1) use this list
    data1=[78, 23, 199, 200, -66, -17, 50, 230,
           -992, 8, 0, 444, 55, -32, -49, 122, 440]

    Add all the negative numbers
    find the highest negative number
    find the least negative number
    find the avg value of negative number'''
data1 = [78, 23, 199, 200, -66, -17, 50, 230,
         -992, 8, 0, 444, 55, -32, -49, 122, 440]

# negative no
count = 0
for i in data1:
    if 0 > i > -999:
        count += i
print(count)

negative_number = []
negative_count = 0
for i in data1:
    if i < 0:
        negative_number.append(i)
        negative_count = negative_count + 1
        highest_negative_number = max(negative_number)
        least_negative_number = min(negative_number)
        avg_negative_number = (sum(negative_number)/len(negative_number))
print(highest_negative_number)
print(least_negative_number)
print(avg_negative_number)
