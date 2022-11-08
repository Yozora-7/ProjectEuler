"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
def maxPrimeFactor(n):
   # number must be even
   while n % 2 == 0:
      max_Prime = 2
      n /= 1
   # number must be odd
   for i in range(3, int(math.sqrt(n)) + 1, 2):
      while n % i == 0:
         max_Prime = i
         n = n / i
   # prime number greater than two
   if n > 2:
      max_Prime = n
   return int(max_Prime)

n = 600851475143
print(maxPrimeFactor(n))
