# N is no of int in array
# Q is No of queries
# l is array of int N
# k is key 
# k=1 max num
# k=2 min num


# we have to find the sum of queries acc to key value

# for example
# N=3  Q=1
# l=13 30303 47
# k=1 query=2

# O/p =>  4+9=13
# --------------------
# k=2 query=1
# O/P => 2



N,Q=map(int,input().split())
l=input().split(' ')
c=0
def sumofdigits(n):
    if len(n)==1:
        return n
    else:
        c=0
        for i in n:
            c=c + int(i)
        c=str(c)
        return sumofdigits(c)
f=list(map(sumofdigits,l))
f=[int(i) for i in f]
f.sort()
for i in range(Q):
    k,query=map(int,input().split())
    if k==1:
        num=-1
        s=0
        for i in range(query):
            s=s+f[num]
            num=num-1
        print(s)
    else:
        num=0
        s=0
        for i in range(query):
            s=s+f[num]
            num=num+1
        print(s)