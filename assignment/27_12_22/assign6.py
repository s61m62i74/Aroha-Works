'''2) emp={100: ('Anand', 'Sales', 56400, 200: ('Vijay', 'Purchase', 67200), 333: ('Vani', 'Purchase', 37200), 220: ('Harish', 'Logistics', 32200),
              440: ('Vinay Vittal', 'Software', 75200), 289: ('Prakash Rao', 'Sales', 50000), 176: ('John Abraham', 'Software', 52000)}

process and do the following:
you must use loop, when the user types STOP or QUIT or DONE - the control should come out
a) accept the dept name and display all the employ name with salary of THAT department

    once done....try this...again loop concepts should be used...here if -1 then STOP
    b) accept the salary and display all the employ details who are drawing a salary above the accepted value

    once done....try this...again loop concepts should be used...here if -1 then STOP
    c) accept the key, if it exists display the employ details otherwise display 'No such emp code exists '
    keep a track how many emp codes were NOT found

    d) for the above how will you achieve this(bit challenging)
    input the empcode if you had already inputted it then - display the empcode you have tried
    otherwise dispaly the emp details OR emp code DOES not exists'''

emp = {100: ('Anand', 'Sales', 56400), 200: ('Vijay', 'Purchase', 67200), 333: ('Vani', 'Purchase', 37200), 220: ('Harish', 'Logistics', 32200),
       440: ('Vinay Vittal', 'Software', 75200), 289: ('Prakash Rao', 'Sales', 50000), 176: ('John Abraham', 'Software', 52000)}

user_input = input('STOP or QUIT or DONE - the control should come out:')
while user_input not in ['stop', 'STOP', 'QUIT', 'quit', 'done', 'DONE']:
    a = list(emp.values())
    dept = input('department name:')
    for key, value in emp.items():
        if value[1] == dept:
            print(value[0], value[2])
    accpt_sal = int(input('enter eccepted value:'))
    for key, value in emp.items():
        if value[2] > accpt_sal:
            print(value[0], value[1])
    count = 0
    accpt_key = int(input('enter the key:'))

    for key in emp:
        if key != accpt_key:
            print('not exist')
            break
        else:
            print(emp[key])
            break
    if key != accpt_key:
        count += 1
    print(f'how many emp codes were NOT found:{count}')
