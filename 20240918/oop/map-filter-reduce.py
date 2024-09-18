nums = [2,3,4]
#map syntax
#map(<func>,iterable)
nums_sqr = list(map(lambda num: num**2, nums))
print(nums_sqr)
nums_even = list(filter(lambda num: num % 2 ==0, nums))
print(nums_even)
from functools import reduce 
nums = [10,20,30, 41]
nums_sum = reduce(lambda s,num: s+ num, nums,0) #101
nums_prod = reduce(lambda p,num: p * num, nums,1) #246000
print(nums_sum, nums_prod)

import sys
nums_min = reduce(lambda m,num: min(m,num), nums,sys.maxsize) #10
nums_max = reduce(lambda m,num: max(m,num), nums,-sys.maxsize) #41
print(nums_min, nums_max)
nums_min = reduce(min, nums) #10
nums_max = reduce(max, nums) #41
print(nums_min, nums_max)