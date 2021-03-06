#===
#Highly divisible triangular number
#
#Problem 12
#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#
#What is the value of the first triangle number to have over five hundred divisors?
#===

def list_divisors_brute_force(n):
    if n < 2:
        return [1]
    div_list = [1]
    for d in range(2, int(pow(n, 0.5) + 1)):
        if n%d == 0:
            div_list.append(d)
            div_list.append(n//d)
    return div_list
	
def tri_divisors(n, divs_limit = 499):
    max_divs = 0
    for i in range(1, n+1):
        tri = i*(i+1) // 2
        divisors = list_divisors_brute_force(tri)
        num_divs = len(divisors)
        if num_divs > max_divs:
            divisors.sort()
            max_divs = num_divs
            print(i, tri, num_divs)
            if max_divs > divs_limit:
                break

tri_divisors(20000)