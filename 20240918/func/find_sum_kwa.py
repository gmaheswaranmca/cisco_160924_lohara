def find_sum(first, second, **others):
    s = first + second 
    if(len(others) > 0):
        for key in others:
            s += others[key]
        #end for 
    #end if 
    #print(type(others))
    return s 
print(find_sum(first=10, second=20)) #30 
print(find_sum(first=10, second=20, third=30)) #60 
print(find_sum(first=10, second=20, third=30, fourth=40, fifth=50)) #150 
