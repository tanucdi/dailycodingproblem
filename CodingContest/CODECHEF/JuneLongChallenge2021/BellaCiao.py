t=int(input())
for i in range(t):
    D,d,P,Q=input().split()
    D=int(D)
    d=int(d)
    P=int(P)
    Q=int(Q)
    a=0
    i=0
    s=0
    if D%d!=0:
        while i<(D//d)+1:
            if i==D//d:
                s=s+(P+(a*Q))
            else:
                s=s+(P+(a*Q))*d
            i+=1
            a+=1
        print(s)
    else:
        while i<(D//d):
            s=s+(P+(a*Q))*d
            i+=1
            a+=1
        print(s)