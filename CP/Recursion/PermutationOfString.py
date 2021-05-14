result=[]
def cal(data,i,n):
    if i ==n:
        result.append(''.join(data)) #A B C
    for j in range(i,n+1):
        data[i],data[j]=data[j],data[i]
        cal(data,i+1,n)
        data[i],data[j]=data[j],data[i] #BACKTRACKING

'''
data='abc'
i=0
n=len(data)-1
'''
cal(list('abc'),0,2)
print(result)