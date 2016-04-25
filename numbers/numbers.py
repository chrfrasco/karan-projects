import math
import itertools

def pi_to_n_dp(n):
	return round(math.pi, n)

def e_to_n_dp(n):
	return round(math.e, n)

def fibb(n, upto=True):
	if upto:
		i, j = 0, 1
		while j < n:
			i, j = j, i+j
		return j - (j-i)
	else:
		i, j = 0, 1
		for _ in range(n-1):
			i, j = j, i+j
		return j

def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False

    return True

def next_prime():
	primes = (i for i in itertools.count() if is_prime(i))
	response = ''
	print("First prime is {0}".format(next(primes)))
	while not response:
		response = input("Press enter for the next prime or type exit: ")
		print(next(primes))
	pass

tile_cost = lambda cost, width, height: cost * width * height

def mortgage_calc():
