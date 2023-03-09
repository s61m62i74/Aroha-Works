'''1) input 5 students marks in 3 subjects
   find the total, avg
   the passing avg is 50 and above

   find out how many students passed.
   find out what is the highest and lowest avg

HINT: use 2 nested loops

attempt the above in both: 1 time use for loop,  next time try with while loop
'''

avg_list = []
for i in range(1, 6):  # students
    sub_list = []
    print(f"Student {i} marks:\n")
    for j in range(1, 4):
        sub = int(input(f"Please enter the marks of subject {j}: "))
        sub_list.append(sub)
    avg_sub = sum(sub_list)/3
    avg_list.append(avg_sub)
    if avg_sub >= 50:
        print(f"---Student {i} is passed with {round(avg_sub, 2)} average---")
    else:
        print(f"---Student {i} is failed with {round(avg_sub, 2)} average---")
    print("*"*80)
    print("*"*80)

print(f"Highest average is: {max(avg_list)}")
print(f"Lowest average is: {min(avg_list)}")
print("*"*80)
print("*"*80)
