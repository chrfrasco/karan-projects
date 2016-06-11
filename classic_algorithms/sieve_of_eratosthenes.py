from math import sqrt, ceil

def sieve(upto):
    A = [0, 0] + [True]*(upto-1)
    primes = []
    for i in range(2, ceil(sqrt(upto))):
        if A[i]:
            for j in range(i**2, upto, i):
                A[j] == False
    print(A)
    return [num*boo for num, boo in zip(range(upto), A)]

print(sieve(30))
