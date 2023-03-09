'''1) given.....
    data1=(10, 22, 67, 100, 200, 400, 22, 500, 35, 250)
    find out how many 2 digit numbers are there in the above data1
    procesing the LAST FIVE elements only'''  # condition - the processing should stop when the count is 3
data1 = (10, 22, 67, 100, 200, 400, 22, 500, 35, 250)
data2 = data1[-1:-6:-1]

count = 0
for i in data2:
    if 10 <= i <= 99 or -99 <= i <= -10:
        count += 1
        if count == 3:
            break
print(count)
