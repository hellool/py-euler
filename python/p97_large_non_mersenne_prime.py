#find the last 10 digits of 28433 * 2^(7830457) + 1, which we will call N
#key is the power of 2, which is too large to efficiently deal with
#we can use modular arithmetic to help us out here.
#since we are only interested in the last 10 digits, we can compute N modulo (10^10)
#this is convenient since it is efficient to do repeated powers modulo relatively small numbers.
# we can use the optional 3rd argument of python's native pow() function to do this.

x = pow(2, 7830457, 10**10) #this is 2^7830457 (mod 10^10), aka its last 10 digits.
n_mod = (x * 28433 + 1) % (10**10)
print(n_mod)

#alternatively we could have used a loop if we didn't use a modular power function
x = 1
for i in range(7830457):
    x = (x * 2) % (10**10) #double x and then take the last 10 digits of it
n_mod = (x * 28433 + 1) % (10**10)
print(n_mod)
