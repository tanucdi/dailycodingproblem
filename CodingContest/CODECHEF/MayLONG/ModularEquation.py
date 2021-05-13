t=int(input())
for i in range(t):
    n,m=input().split()
    n=int(n)
    m=int(m)
    c=0
    # creating list [1,1,1,1] n=3
    l=[1]*(n+1)
    a=2
    while a<=n:
        x=m%a
        c+=l[x]
        b=x
        while b<=n:
            l[b]=l[b]+1
            b+=a
        a+=1
    print(c)