#OPTIMAL SOLUTION. ALL TEST CASE PASSED. 
numSeq=[2,1,4,3]
fp=0
sp=0
for i in range(len(numSeq)):
    if i%2==0:
        fp=fp+numSeq[0]
    else:
        sp=sp+numSeq[0]
    if numSeq[0]%2==0:
        numSeq.remove(numSeq[0])
        numSeq.reverse()
    else:
        numSeq.remove(numSeq[0])
print(fp-sp)