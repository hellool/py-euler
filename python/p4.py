# -*- coding: utf-8 -*-

#Problem 4: Largest Palindrome Product
#Find the largest palindrome made from the product of two 3-digit numbers.

#See the doc "operations on digits" for a dicussion of a common technique used in this solution

largest = 0

def is_palindrome(n):
    string_n = str(n)
    for i in range(len(string_n)):
        if string_n[i] != string_n[(-1)*(i+1)]:
            return False #not a palindrome
    return True

for n1 in range(100, 1000): #100-999
    for n2 in range(100, 1000):
        prod = n1*n2
        if is_palindrome(prod):
            if prod > largest:
                largest = prod
                print(prod) #dangerous if number range is too large. 3 digits should be ok

print("answer: {}".format(largest))
        
        