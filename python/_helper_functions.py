## Brett McLean
## This module contains code for various helper functions that can be reused in multiple challenge problems

import numpy


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