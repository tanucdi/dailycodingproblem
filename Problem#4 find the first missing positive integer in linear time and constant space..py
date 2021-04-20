# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

l=[3,4,-1,1]
l.sort()
for i in range(1,len(l)+1):
    if i not in l:
        print(i)
        break
else:
    print(l[-1]+1)