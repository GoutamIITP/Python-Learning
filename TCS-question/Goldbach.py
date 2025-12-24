""" How can a number be expressed as a sum of two prime numbers?
write a program. """

def isPrime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  else:
    return True
      
def findPrimeSum(num):
  found = False
  for i in range(2, num // 2 + 1):
    if isPrime(i) and isPrime(num - i):
      print(f"{num} can be expressed as the sum of {i} and {num - i}.")
      found = True
      break
  
  if not found:
    print(f"{num} cannot be expressed as the sum of two prime numbers")
 

n = int(input())
findPrimeSum(n)