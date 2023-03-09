# account number functions-->

#import pandas as pd
customer_info = {}

while True:
    cu_list = []
    acc_list = []
    phn_list = []
    email_list = []
    cu_name = input("enter name: ")  # customer name
    acc_num = input('enter account number:')  # account number
    cu_phn_n = input('enter phone number:')  # custumer phone number
    email_id = input('enter email:')  # custumer email id


# length check

    def ch_le(acc_num):
        if 7 <= len(acc_num) <= 12:
            return True


# check 1st 3 char must be alphabet

    if ch_le(acc_num) == True:
        def ch_alp(acc_num):
            res = acc_num[0:3:1]
            count = 0
            for i in res:
                if 64 < ord(i) < 91 or 96 < ord(i) < 123:
                    count += 1
            if count == 3:
                return True


# find the given str is starts from S C F R D
    if ch_alp(acc_num) == True:
        def st_chr(acc_num):
            if acc_num[0] in 'scfrdSCFRD':
                return True


# find whether the given string is number except 1st 3char
    if st_chr(acc_num):
        def exc_char(acc_num):
            ext = acc_num[3:len(acc_num):1]
            for i in ext:
                if i not in '0123456789':
                    return False
            return True
    if exc_char(acc_num) == True:
        acc_list += [acc_num]
    else:
        print("Invalid account...!!!")


# phone number check function

    def ch_phn_n(cu_phn_n):
        if len(cu_phn_n) == 10:
            for i in cu_phn_n:
                if not (0 <= int(i) <= 9):
                    return False
                else:
                    return True
    if ch_phn_n(cu_phn_n) == True:
        phn_list += [cu_phn_n]
    else:
        print("Invalid phone...!!!")


# check for email


    def ch_mail(email_id):
        if email_id[0] == '@' or email_id[-1] == '@':
            return False
        a = 0
        for i in range(1, len(email_id)-1):
            if email_id[i] == '@':
                a += 1
        if a == 1:
            return True
    if ch_mail(email_id) == True:
        email_list += [email_id]
    else:
        print("Invalid email...!!!")


# check name

    def ch_name(cu_name):
        for i in cu_name:
            if not ('a' <= i <= 'z') or not ('A' <= i <= 'z'):
                return False
        else:
            return True
    if ch_name(cu_name) == True:
        cu_list += [cu_name]

    print('list of acc number:', acc_list)
    print('list of customer :', cu_list)
    print('list of phone number:', phn_list)
    print('list of email:', email_list)

    if len(acc_list) and len(phn_list) and len(email_list) in [0]:
        break
    else:
        pass

    def add_info():

        for name, acc, phn_no, mail in zip(cu_list, acc_list, phn_list, email_list):
            if 'NAME' not in customer_info:
                customer_info['NAME'] = [name]
            else:
                customer_info['NAME'] += [name]

            if 'ACC' not in customer_info:
                customer_info['ACC'] = [acc]
            else:
                customer_info['ACC'] += [acc]

            if 'PHONE' not in customer_info:
                customer_info['PHONE'] = [phn_no]
            else:
                customer_info['PHONE'] += [phn_no]

            if 'MAIL' not in customer_info:
                customer_info['MAIL'] = [mail]
            else:
                customer_info['MAIL'] += [mail]

        print(customer_info)
    add_info()


print(customer_info)
