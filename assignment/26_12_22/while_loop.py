avg_list = []
i = 1
while i < 6:
    sub_list = []
    print(f"Student {i} marks:\n")
    i += 1
    j = 1
    while j < 4:
        sub = int(input(f"Please enter the marks of subject {j}: "))
        sub_list.append(sub)
        j += 1
    avg_sub = sum(sub_list)/3
    avg_list.append(avg_sub)
    if avg_sub >= 50:
        print(f"---Student {i} is passed with {round(avg_sub, 2)} average---")
    else:
        print(f"---Student {i} is failed with {round(avg_sub, 2)} average---")

print(f"Highest average is: {max(avg_list)}")
print(f"Lowest average is: {min(avg_list)}")
