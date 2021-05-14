''' 
GIVEN A RANGE OF THE FORM [L,R]. THE TASK IS TO PRINT ALL THE SEXY PRIME PAIRS IN THE RANGE.

Examples:
Input = L=1 R=19
Output = (5,11) (7,13) (11,17) (13,19)
'''

from math import sqrt
def check(n):
    l=[True]*(n+1)
    l[0]=False
    l[1]=False
    for i in range(2,int(sqrt(n))+1):
        if l[i]==True:
            for j in range(i*i,n+1,i):
                l[j]=False
    return l

L=6
R=59
myprime=check(R)

for i in range(L,len(myprime)-6):
    if myprime[i]==True:
        x=i
        y=x+6
        if myprime[y]==True:
            print(f'({x},{y})')