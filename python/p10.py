#===
#Summation of primes
#
#Problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.
#===

#This is a good problem to test the Miller-Rabin algorithm that we made, although a sieve is certainly good enough to solve it for N= 2 million
#This code takes about 5 seconds to run on my PC.
from _helper_functions import is_prime

total = 2 #for convenience on the range function we start at 3
for n in range(3, 2000000, 2):
    if is_prime(n):
        total += n

print(total)