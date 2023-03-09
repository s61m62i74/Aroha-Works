'''3) create a list called names
   add names of your friends / colleagues etc
   keep adding names till the user types ANY one of these
   STOP
   QUIT
   DONE

   using the for loop display all the added names
   how many names were added?
   if there anyone with the following names , if it is there then display YES it is there.
   Asha
   Vikram
   Rakesh
   Bhaskar

   suppose there is name added Anita
   how will you replace that name as 'Anita Prasad' ?
'''
name1 = 'DHIVAKAR'
name2 = 'MOHAN'
name3 = 'KUMAR'
name4 = 'SURYA'
count = 0
names = []


while True:
    print()
    loop = input(
        'enter anythibg to countinue , enter STOP or QUIT or DONE to STOP : ')
    loop = loop.upper()

    if loop == 'QUIT' or loop == 'DONE' or loop == 'STOP':

        break

    else:

        input_name = input('ENTER THE NAME : ')

        names.append(input_name.upper())

for i in names:

    print(i, end=' , ')

    count += 1

for i in names:

    if i == name1 or i == name2 or i == name3 or i == name4:
        print('\n')
        print('***** ', i, ', YES, THIS NAME IS THERE *****')

print('\n')
print('COUNT OF NAMES IS : ', count)
print()
print(names)
print()
old_name = input('ENTER WHICH NAME YOU WANT TO REPLACE : ')
print()
new_name = input('ENTER THE NEW NAME : ')
old_name = old_name.upper()
new_name = new_name.upper()
print()
for i in range(len(names)):

    if names[i] == old_name:

        names[i] = new_name

print(names)
