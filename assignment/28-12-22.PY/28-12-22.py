Names = input('enter names:')


def name(a):
    l = a.split()
    new = ""
    for i in range(len(l)-1):
        a = l[i]
        new += (a[0].upper()+'.')
    new += l[-1].title()
    return new


print(name(Names))
