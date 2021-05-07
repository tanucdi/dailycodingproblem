t=int(input())
for i in range(t):
    X,A,B=input().split()
    s=int(A)+(100-int(X))*int(B)
    s=s*10
    print(s)