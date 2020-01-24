## Brett McLean
## This module contains code for various helper functions that can be reused in multiple challenge problems

import numpy as np
import math
import random

#Given a vector of numbers, this function normalizes it to the unit vector in the same direction with length 1
def unit_vector(v):
    mag = pow(sum([x**2 for x in v]), 0.5)
    v_unit = [x / mag for x in v]
    return v_unit
    
#This function computes the smallest angle between two input vectors, subject to float rounding error. 
#Returns a value between 0 and pi radians.
#If as_degrees==True, then returns a value between 0 and 180 degrees instead.
def angle_between(v1, v2, as_degrees=False):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    
    angle = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    if as_degrees:
        return (180/math.pi) * angle
    else:
        return angle
    
#This function returns True if n is prime and False if n is composite.
#The method used to determine primality depends on the size of n
# if n <= 100, we just check against a short list of primes<100
# if n <= 10000, we use the same list in a sieve method
# if n > 10000 we will use the Miller-Rabin test for primality
def is_prime(n):
    if n>2 and n%2 == 0:
        return False
    if type(n) != int:
        if int(n) == n:
            n = int(n)
        else:
            print("Warning: {} is not an integer in prime test".format(n))
            return False
    primes_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n <= 10000:
        if n <= 100:
            return (n in primes_100)
        else:
            for p in primes_100:
                if n%p == 0:
                    return False
            return True
    
    else: #use Miller-Rabin
        r = 0
        d = 0
        
        x = n-1
        while x%2 == 0:
            r += 1
            x = x // 2
        d = x 
        #d will always be odd since n is odd
        # n = [2^r * d] + 1
        
        #per wikipedia: if n < 3,474,749,660,383 (3.47e13), it is enough to test a = 2, 3, 5, 7, 11, and 13 (First 6)
        #if n < 3,317,044,064,679,887,385,961,981, (3.31e25), it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, and 41 (First 13)
        if n < 3*10**12:
            K = 6
        elif n < 3*10**24:
            K = 13
        else:
            K = int(math.log(n, 10)) #K roughly equal to number of digits
        
        for i in range(K):
            witness = False
            if i <= 20:
                a = primes_100[i]
                #for early iterations, use small primes for a
            else:
                a = random.randint(15, n-2)
                
            x = pow(a,d,n)
            if x == 1 or x == (n-1):
                continue #witness to primality
                
            for j in range(r-1):
                x = pow(x,2,n)
                if x == (n-1):
                    witness = True #witness to primality
                    break
            if witness:
                continue
            else:
                return False #composite
        
        return True #probably prime

#This function returns an ordered list of prime numbers less than `max_n`
#Alternatively return an ordered list of the first `max_primes` prime numbers.
#Be careful with large values of n
#max_n cannot be less than 3
#if `as_set` is true, return a set instead of a list
def generate_primes(max_n = 100, max_primes = None, as_set = False):
    if max_n != None and max_primes != None:
        print("Error in generate_primes(): max_n = {} and max_primes = {}. exactly one of max_n and max_primes must be specified and the other set to None.".format(max_n, max_primes))
        return []

    if max_n:
        if max_n < 2:
            return []

        primes = [2]
        for n in range(3, max_n, 2):
            for p in primes:
                if n%p == 0:
                    break # n is composite if p divides n
                if p*p > n:
                    primes.append(n)
                    break # n is prime if we reach a prime larger than the square root of n, since that means we checked all possible divisors
    
    elif max_primes:
        if max_primes < 1:
            return []
        primes = [2]
        num_primes = 1
        
        n = 3
        while num_primes < max_primes:
            for p in primes:
                if n%p == 0:
                    break # n is composite if p divides n
                elif p*p > n:
                    primes.append(n)
                    num_primes += 1
                    break # n is prime if we reach a prime larger than the square root of n, since that means we checked all possible divisors
            n += 2
    
    if as_set:
        return set(primes)
    else:
        return primes
           
##test with this list of 3 50 digit numbers. the first two are known primes, the third is composite
#for i in [22953686867719691230002707821868552601124472329079,30762542250301270692051460539586166927291732754961,30762542250301270692461460539586166927291732754961]:
#    print(i, is_prime(i))
    