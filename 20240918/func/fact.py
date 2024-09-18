def fact(N):
    if N <= 1:#base/edge case
        return 1
    #endif
    return N * fact(N-1)

print(fact(5)) #120
print(fact(4)) #24 