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
Cubes = (1, 8, 27, 64, 125, 216)
cube = iter(Cubes)
next(cube)
print(next(cube))