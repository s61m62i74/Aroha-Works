name = input('enter your name:')
var = name.split()
out = ''
for i in var:
    if len(var) == 1:
        out += i.upper()
    else:
        out += i[0].upper() + " "
print(out)
