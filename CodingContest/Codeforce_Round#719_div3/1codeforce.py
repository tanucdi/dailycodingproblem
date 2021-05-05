# B. Ordinary Numbers
# time limit - per test2 seconds
# memory limit - per test256 megabytes


# Let's call a positive integer n ordinary if in the decimal notation all its digits are the same. For example, 1, 2 and 99 are ordinary numbers, but 719 and 2021 are not ordinary numbers.

# For a given number n, find the number of ordinary numbers among the numbers from 1 to n.

# Input
# The first line contains one integer t (1≤t≤104). Then t test cases follow.

# Each test case is characterized by one integer n (1≤n≤109).

# Output
# For each test case output the number of ordinary numbers among numbers from 1 to n.

# Example
# inputCopy
# 6
# 1
# 2
# 3
# 4
# 5
# 100
# outputCopy
# 1
# 2
# 3
# 4
# 5
# 18


def fun(t):
    c=0
    for j in range(1,int(t)+1):
        n=str(j)
        s=0
        for i in range(len(n)):
            s=s+(int(n[i]))*(10**i)
            if int(n)==s:
                c=c+1
    print(c)

testcase=int(input())
for test in range(testcase):
    t=input()
    fun(t)

#CODE WORKED BUT TIME LIMIT EXCEEDS. NOT OPTIMAL SOLUTION