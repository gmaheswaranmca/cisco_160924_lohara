a = list('nithin')#noteis
a[1::2]='oes'
a = ''.join(a)
print(a)

x = [1,2,3,4,5,6]#odd pos cube, even pos sqr wher pos is 1-based index
print(x)
x[0::2] = (e**3 for e in x[0::2] )
x[1::2] = (e**2 for e in x[1::2] )
print(x)
