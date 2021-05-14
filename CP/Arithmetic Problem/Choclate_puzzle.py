#TIME COMPLEXITY
# inp=5 | 2,4,8,16,32 = 62
# we can do it usinng loop but tc will be O(n)
# but here using GP tc is O(1)


n=int(input())
r=a=2
s=0
s=(a*(r**n - 1))
r=r-1
s=s//r
print(s)