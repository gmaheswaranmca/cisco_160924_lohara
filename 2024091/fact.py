def find_fact(N:int)->int:
    fact = 1
    for I in range(N, 1, -1):
        fact = fact * I 
    return fact

f1 = find_fact(5) #120
f2 = find_fact(4) #24
print(f1)
print(f2)