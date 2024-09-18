import math
def is_prime(N):
    N_sqrt = int(math.sqrt(N))
    for I in range(2,N_sqrt+1):
        if N % I == 0:
            return False 
        #endif 
    #endfor 
    return True 

print(is_prime(5))
print(is_prime(51))
print(is_prime(60))
print(is_prime(61))