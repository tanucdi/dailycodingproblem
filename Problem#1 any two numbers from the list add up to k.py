# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

l=[10, 15, 3, 7]
k=int(input())
i=0
while(i<len(l)):
    j=1
    while(j<=len(l)-1):
        if(l[i]+l[j]==k):
            print('True',l[i],l[j])
            break
        j=j+1
    i=i+1
