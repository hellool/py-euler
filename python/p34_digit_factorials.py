#===
#Digit factorials
#
#Problem 34
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#===
#
#9! = 362880, the largest a single digit can contribute to the equation.
#that means if n gets big enough, no amount of 9s could make the sum of digit factorials greater than n.
#
#999,999 < 6*(9!) = 2,177,280
#9,999,999 > 7*(9!) = 2,540,160
#
#This means no solution can have more than 7 digits. We can find an ideal bound, but even the original 10 million is good enough to solve this problem.

import math

max_n = 10**7
total = 0
for n in range(3, max_n): #skip 1=1! and 2=2! as they are not included
    if n%max_n == (max_n//10):
        print("{}%".format(max_n//n))
    list_n = [int(x) for x in str(n)] #list of digits as ints
    fact_sum = sum([math.factorial(x) for x in list_n])
    if n == fact_sum:
        print(n, list_n)
        total += n
print(total)
        