# n=int(input())
# def convert_to_words(num):
#     l = len(num)
#     single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     two_digits = ["", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen","nineteen"]
#     tens_multiple = ["", "", "twenty", "thirty", "forty","fifty", "sixty", "seventy", "eighty", "ninety"]
#     if (l == 1):
#         print(single_digits[ord(num[0]) - 48])
#         return
#     for i in range(1):
#         if (ord(num[0]) - 48 == 1):
#             sum = (ord(num[0]) - 48) + (ord(num[1]) - 48)
#             print(two_digits[sum])
#             return
#         elif (ord(num[0]) - 48) == 2 and (ord(num[1]) - 48)== 0:
#             print("twenty")
#             return
#         else:
#             i = ord(num[0]) - 48
#             if(i > 0):
#                 print(tens_multiple[i], end="")
#             if (ord(num[1]) - 48 )!= 0:
#                 print('-'+single_digits[ord(num[1]) - 48])

# convert_to_words(str(n))
# Python code for calculating number of ways
# to distribute m mangoes amongst n people
# where all mangoes and people are identical


# function used to generate binomial coefficient
# time complexity O(m)

def binomial_coefficient(n, m):
	res = 1
	if m > n - m:
		m = n - m

	for i in range(0, m):
		res *= (n - i)
		res /= (i + 1)
	return res
def calculate_ways(m, n):
	if m<n:
		return 0
	ways = binomial_coefficient(n + m-1, n-1)
	return int(ways)

m = int(input())
n = int(input())
result = calculate_ways(n, m)
print(result)
