import os
first_name = input("enter first name:")
last_name = input("enter last name:")

variable = os.path.exists('userdata.txt')
if (variable == True):
    user = open('userdata.txt', 'a')
    user.write("\n" + first_name+' '+last_name)
else:
    user = open('userdata.txt', 'w')
    user.write(first_name+' '+last_name+"\n")
print(user)
