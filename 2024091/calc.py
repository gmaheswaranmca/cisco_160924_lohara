def calc(first:int, second:int)->int:
    sum = first + second 
    diff = first - second 
    product = first * second 
    quotient = first // second 
    return sum, diff, product, quotient 


s,d,p,q = calc(20,6) #26,14,120,3
print(s,d,p,q)

t1 = calc(10,6) #(16,4,60,1)
print(t1)
print(type(t1))