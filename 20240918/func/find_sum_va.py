def find_sum(first, second, *others):
    s = first + second 
    if(len(others) > 0):
        for num in others:
            s += num
        #end for 
    #end if 
    #print(type(others))
    return s 
print(find_sum(10, 20)) #30 
print(find_sum(10, 20, 30)) #60 
print(find_sum(10, 20, 30, 40, 50)) #150 
