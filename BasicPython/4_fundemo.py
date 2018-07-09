# ===================================================================
# function to calculate factors of n
# ===================================================================
def factors(n):
	# list to store factors of n	
	fl = []	
	# iterate from 1 to n
	for i in range(1, n+1):
		if n%i == 0:
			# append the value to the list
			fl.append(i)
	# return the factor list		
	return fl
	
# ===================================================================
# function to calculate the GCD
# ===================================================================
def gcd(m,n):
	# if m is less than n, then swap the values
	if m < n:
		(m,n) = (n,m)
	# keep on reducing m till we get gcd
	while m%n != 0:
		(m,n) = (n,m%n)
	return n	

# ===================================================================
# function to find prime numbers in n
# ===================================================================
def prime_in_n(n):
	res = []	
	for i in range(1, n+1):		
		# prime no has only 2 factors
		if(factors(i) == [1,i]):
			res.append(i)
			# print(f"{i} is prime")
	return res

# ===================================================================
# function to find first n prime numbers
# ===================================================================
def n_prime(n):
	count = 0;
	i = 2
	res = []
	# iterate till we get n prime nos
	while count < n:
		if(factors(i) == [1,i]):
			res.append(i)
			count = count + 1
		i = i + 1
	return res

# ===================================================================
# function returning multiple values, number its square & cube
# ===================================================================
def square_cube(val):
	v1 = val ** 2;
	v2 = val ** 3;	
	return val, v1, v2;
	
# ===================================================================
# function call
# ===================================================================
print(f"factors(5)  is {factors(5) }")
print(f"factors(10) is {factors(10)}")
print(f"factors(56) is {factors(56)}")
print()
print(f"gcd(14,56) is {gcd(14,56)}")
print(f"gcd(36,56) is {gcd(36,56)}")
print(f"gcd(36,60) is {gcd(36,60)}")
print()
print(f"prime_in_n(36) is {prime_in_n(36)}")
print()
print(f"n_prime(13) is {n_prime(13)}")
print()
n,s,c = square_cube(10);
print(f"square_cube(10) is {n}^1:{n}, {n}^2:{s} & {n}^3:{c}");


