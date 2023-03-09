#data1=['ramesh kumar sharma','sambit dash']
# o/p=fname=ramesh       sambit
# mname=kumar
# lname=sharma           dash

Name = ['surjit sahu', 'sambit dash', 'shuvam mohapatra',
        'surya prasad moharana', 'soumya anurag mohapatra']
for i in Name:
    names = i.split()
    if len(names) == 2:
        print("there is no middle name")
        first_name = names[0]
        last_name = names[1]
        print(f" first name - {first_name}\n last name - {last_name}")
    elif len(names) == 3:
        print("there is  middle name")
        first_name = names[0]
        middle_name = names[1]
        last_name = names[2]
        print(
            f" first name - {first_name}\n middle name - {middle_name} \nlast name - {last_name}")
