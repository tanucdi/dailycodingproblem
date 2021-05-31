'''
It’s Chef's birthday. He and his twin have received N gifts in total. The i-th gift has a price of Ai. Each twin wants to keep the most expensive gifts for himself.

The twins take K turns alternately (each has K turns, for 2⋅K turns in total). It is given that 2⋅K+1≤N. In a turn, a person may choose one gift. The only exception is the last turn of the twin who moves second, where he gets to choose two gifts instead of one. Assuming they both choose gifts optimally and you can choose who takes the first turn, find the maximum total cost of the gifts that Chef keeps.

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains two lines of input.
The first line contains two space-separated integers N, K.
The second line contains N space-separated integers A1,A2,…,AN, the price of the gifts.
Output
For each test case, output in a single line the answer to the problem.

Constraints
1≤T≤100
3≤N≤103
1≤K≤N−12
1≤Ai≤109
Subtasks
Subtask #1 (100 points): original constraints

Sample Input
3
3 1
1 3 2
3 1
3 1 3
5 2
5 1 3 2 4
Sample Output
3
4
8
Explanation
Test Case 1: Chef moves first and he chooses the gift with cost 3. His twin then chooses the gifts of costs 1 and 2.

Test Case 2: Chef allows his brother to choose first and his brother chooses a gift with cost 3. Then Chef chooses the remaining gift with cost 3. Since Chef moves second, he is allowed to choose one more gift, so he chooses gift with cost 1. The total cost of Chef's gifts is 3+1=4.

Test Case 3: Chef moves first and at the end he will have the gifts with costs 5 and 3. Hence, the total cost of gifts with Chef = 5+3=8.
'''
t=int(input())
for i in range(t):
    n,k=input().split()
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    s1=0
    s2=0
    for i in range(2*int(k)):
        if i%2==0:
            s1=s1+a[i]
        else:
            s2=s2+a[i]
    else:
        s2=s2+a[2*int(k)]
    if s1>s2:
        print(s1)
    else:
        print(s2)