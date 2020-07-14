#1000-digit Fibonacci number
#   
#Problem 25
#The Fibonacci sequence is defined by the recurrence relation:
#
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
#===

#Fortunately for us, Python natively handles large numbers pretty well without an additional package, 
#expanding the memory of the integer object as needed.

import math

#This function prints the Fibonacci numbers through either the Nth number, 
#or until the last number with `max_digits` or less digits, whichever comes first.
#It then prints the first number that exceeds this thresheld i.e. the first Fibonacci number with `max_digits + 1` digits.
def fib(n, max_digits = 10):
    f_last = 0
    f_current = 1
    dig = 1
    i = 0
    while dig <= max_digits:
        t = f_current + f_last
        f_last = f_current
        f_current = t
        i+=1
        dig = int(math.log(f_current, 10)) + 1
    print(i+1, dig, f_current)
    
   #should print the first fib number with 1000 digits along with the index
fib(1000, max_digits = 999) 

        
            
            
    