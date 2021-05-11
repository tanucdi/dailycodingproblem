# For a given N, find the number of ways to choose an integer x from the range [0,2N−1] 
# such that x⊕(x+1)=(x+2)⊕(x+3), where ⊕ denotes the bitwise XOR operator.

# Since the number of valid x can be large, output it modulo 10**9+7. IMP.

# Input
# The first line contains an integer T, the number of test cases. Then the test cases follow.
# The only line of each test case contains a single integer N.
# Output
# For each test case, output in a single line the answer to the problem modulo 109+7.

# Constraints
# 1≤T≤105
# 1≤N≤105
# Subtasks
# Subtask #1 (100 points): Original Constraints

# Sample Input
# 2
# 1
# 2
# Sample Output
# 1
# 2
# Explanation
# Test Case 1: The possible values of x are {0}.

# Test Case 2: The possible values of x are {0,2}.

###################### MOST OPTIMAL SOLUTION.   O(logy)
def power(x, y, p) :
    res = 1
    x = x % p
    if (x == 0) :
        return 0
    while (y > 0) :
        if ((y & 1) == 1) :
            res = (res * x) % p
        y = y >> 1     
        x = (x * x) % p
    return res

t= int(input())
for i in range(t):
    n=int(input())
    print(power(2,n-1,(10**9)+7))
##########################################


#######################LESS OPTIMAL. TLE-5.01SEC
#--------------------1
# def power(x, y):
# 	res = 1
# 	while (y > 0):
# 		if ((y & 1) != 0):
# 			res = res * x
# 		y = y >> 1
# 		x = x * x
# 	return res

# t= int(input())
# for i in range(t):
#     n=int(input())
#     print(power(2,n-1))

#------------------------2
# n=int(input())
#     c=2**n//2
#     print(c)
#------------------------

#---------------------------3
# n=int(input())
# c=0
# for x in range((2**n)-1):
#     if x^(x+1)==(x+2)^(x+3):
#        c+=1
# print(c)
#---------------------------
