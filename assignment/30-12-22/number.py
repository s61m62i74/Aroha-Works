

while True:
    f = int(input('enter the number:'))  # 1st number
    if 0000 <= f <= 9999:

        l = int(input('enter the number:'))  # 2nd number
        if 0000 <= f <= 9999:

            # calculation part
            c = input("enter the operation you want to perform:+,*,-,//:")
        if (c != '*' and c != '+' and c != '-' and c != '//'):
            print('invalid input ')

        if c == '*':
            mul = f*l
            print(mul)
        elif c == '+':
            add = f+l
            print(add)
        elif c == '-':
            minus = f-l
            print(minus)
        elif c == '//':
            div = f//l
            print(div)
