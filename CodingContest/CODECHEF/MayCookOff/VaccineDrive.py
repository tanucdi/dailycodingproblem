# 5 2 2 2 2 2 2 2 2 2 2 2
import math
m=[]
l=list(map(int,input().split()))
cg=l[0]
p=l[1]
agegroups=sum(l[cg+2:])
cggroup=l[cg+1]
print(cggroup)
for i in range(1,cggroup+1):
    m.append(math.ceil((agegroups+i)/p))
m.sort()
print(m[0],m[-1])