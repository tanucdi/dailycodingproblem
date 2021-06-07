from math import sqrt
def PrimeTill(n):
    l=[True]*(n+1)
    l[0]=False
    l[1]=False
    for i in range(2,int(sqrt(n))+1):
        if l[i]==True:
            for j in range(i*i,n+1,i):
                l[j]=False

    for i in range(2,len(l)):
        if l[i]==True:
            print(i)