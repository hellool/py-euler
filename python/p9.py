# -*- coding: utf-8 -*-

#Problem 8

def euclid_solution(target_L):
	#target_L is the desired total side length or sum of the triple, 1000 in the original problem
	max_m = int(pow(target_L, 0.5) / 2)
	for m in range(1, max_m+1): #ranges from 1 to max_m
		for n in range(1, m): #ranges from 1 to m-1
			L = 2*m*(m+n)
			if L > target_L: 
				break #m, n pair is too large, so reset n to 1 and increase m by 1
			if target_L % L == 0: #hit!
				scaling_factor = target_L // L
				a = scaling_factor * (m**2 + n**2)
				b = scaling_factor * (2*m*n)
				c = scaling_factor * (m**2 - n**2)
				print("Found triple a = {}, b = {}, c = {}. Product = {}".format(a, b, c, a*b*c))
                
euclid_solution(1000)