import math

def binomial(n,k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print(binomial(40,20))