# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

given_list=[1,2,3,4,5]
new_list=[]
for i in range(len(given_list)):
    c=1
    for j in range(len(given_list)):
        if i!=j:
            c=c*given_list[j]
    new_list.append(c)
print(new_list)