# def gcd(a,b):
# 	if (a == 0):
# 		return b
# 	if (b == 0):
# 		return a
# 	if (a == b):
# 		return a
# 	if (a > b):
# 		return gcd(a-b, b)
# 	return gcd(a, b-a)

# def fir(k):
#     l=[]
#     for i in range(1,(2*k+1)+1):
#         A=k+i*i
#         l.append(A)
#     s=0
#     print(l)
#     i=0
#     while i<2*k:
#         g=gcd(l[i], l[i+1])
#         s=s+g
#         i+=1
#     print(s)

# t=int(input()) 1
# for i in range(t):
#     k=int(input())
#     fir(k)
t=int(input())
for i in range(t):
    n,m=input().split()
    n=int(n)
    m=int(m)
    c=0
    b=n
    a=1
    while b>a:
        a=b-1
        while a>=1:
            if (m-(m%b))%a==0:
                c+=1
            a-=1
        b-=1
    print(c)