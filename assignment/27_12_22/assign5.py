'''s1 = { 'GAnesh','ChaRLes', '123666','67.22','SDSDA442rtrt'}
   convert only the names into upper case, non alphabets - should be ignored
  the output should be 
  GANESH
  CHARLES'''
s1 = {'GAnesh', 'ChaRLes', '123666', '67.22', 'SDSDA442rtrt'}

for i in s1:
    out = ''
    for j in i:
        if 'a' <= j <= 'z' or 'A' <= j <= 'Z':
            out += j
    if i == out:
        print(i.upper())
