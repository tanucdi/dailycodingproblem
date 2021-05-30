# Chef knows about two languages spoken in Chefland, but he is not proficient in any of them. The first language contains lowercase English letters between 'a' and 'm' inclusive and the second language contains only uppercase English letters between 'N' and 'Z' inclusive.

# Due to Chef's limited vocabulary, he sometimes mixes the languages when forming a sentence — each word of Chef's sentence contains only characters from one of the languages, but different words may come from different languages.

# You are given a sentence as a sequence of K words S1,S2,…,SK. Determine whether it could be a sentence formed by Chef, i.e. if it contains only the characters from the two given languages and each word contains only characters from a single language.

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains an integer K followed by a space and K space-separated strings S1,S2,…,SK.
# Output
# For each test case, print a single line containing the string "YES" if the given sentence can be formed by Chef or "NO" if it cannot.

# You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

# Constraints
# 1≤T≤105
# 1≤K≤10
# 1≤|Si|≤100 for each valid i
# the sum of lengths of all the strings on the input does not exceed 105
# each string contains only lowercase and uppercase English letters
# Example Input
# 3
# 1 aN
# 2 ab NO
# 3 A N D
# Example Output
# NO
# YES
# NO
# Explanation
# Example case 1: A single word cannot contain characters from both languages.

# Example case 2: This could be a sentence formed by Chef since each word contains only characters from a single language.

# Example case 3: Letters 'A' and 'D' do not belong to either of the two languages.

t=int(input())
for i in range(t):
    l=list(input().split())
    c=0
    for i in range(1,int(l[0])+1):
        s1=0
        s2=0
        for j in l[i]:
            if ord(j)>=97 and ord(j)<=109:
                s1+=1
            if ord(j)>=78 and ord(j)<=90:
                s2+=1
        if s1==len(l[i]) or s2==len(l[i]):
            c+=1
    if c==len(l)-1:
        print('YES')
    else:
        print('NO')