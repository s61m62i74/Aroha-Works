import pandas as pd

customer_info = {}
res_acc_num = []
res_name = []
res_address = []
res_ph_no = []
res_mail = []


def except_three(acc_num):
    res = acc_num[3:len(acc_num)]
    for i in res:
        if i not in '0123456789':
            return False

    if not (6 < len(acc_num) < 13):
        return False

    res = acc_num[0:3]
    count = 0
    for i in res:
        if 64 < ord(i) < 91 or 96 < ord(i) < 123:
            count += 1

    if count != 3:
        return False

    if acc_num[0] in 'scfrdSDFRD':
        return True
    return False


while True:
    user = input("enter num : ")
    if "0" <= user <= "9":

        def add_info():
            for name, mail, acc, ph_num, add in zip(res_name, res_mail, res_acc_num, res_ph_no, res_address):
                if 'NAME' not in customer_info:
                    customer_info['NAME'] = [name]
                else:
                    customer_info['NAME'] += [name]

                if 'ACC-NUMBER' not in customer_info:
                    customer_info['ACC-NUMBER'] = [acc]
                else:
                    customer_info['ACC-NUMBER'] += [acc]
                if 'EMAIL' not in customer_info:
                    customer_info['EMAIL'] = [mail]
                else:
                    customer_info['EMAIL'] += [mail]
                if 'PHONE NUMBER' not in customer_info:
                    customer_info['PHONE NUMBER'] = [ph_num]
                else:
                    customer_info['PHONE NUMBER'] += [ph_num]
                if 'ADDRESS' not in customer_info:
                    customer_info['ADDRESS'] = [add]
                else:
                    customer_info['ADDRESS'] += [add]

    name = input('enter your name:')
    acc_num = input('enter your account number:')
    address = input('enter your current address:')
    ph_no = input('enter your current phone number:')
    email = input('enter your current email id:')

    def length_ph(ph_no):
        if len(ph_no) == 10:
            for i in ph_no:
                if not ('0' <= i <= '9'):
                    return False
            else:
                return True
        else:
            return False

    def check_mail(email):
        if email[0] == '@' or email[-1] == '@':
            return False
        a = 0
        for i in range(1, len(email) - 1):
            if email[i] == '@':
                a += 1
        if a == 1:
            return True
        else:
            return False

    def usename(name):
        for i in name:
            if not ('A' <= i <= 'Z' or 'a' <= i <= 'z'):
                return False
        else:
            return True

    res_address += [address]

    if usename(name) == True and check_mail(email) == True and check_mail(email) and length_ph(ph_no):
        res_acc_num

        add_info()
    else:
        break

    print(res_acc_num)
    print(res_name)
    print(res_address)
    print(res_ph_no)
    print(res_mail)

    print(customer_info)

    add_info()
    break

print(customer_info)
cust = pd.DataFrame(customer_info)
cust.to_csv("customer_info.csv")
print(cust)
