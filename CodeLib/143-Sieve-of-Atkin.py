"""
The Sieve of Atkin is an efficient algorithm used to find all prime numbers upto a given number (say N) and does so in O(N) time complexity.
"""

def SieveOfAtkin(limit): 
    if (limit > 2): 
        print(2 , end = " ") 
    if (limit > 3): 
        print(3 , end = " ") 
    sieve = [False] * limit 
    for i in range( 0 , limit ): 
        sieve[i] = False
    x = 1
    while(x * x < limit ) : 
        y = 1
        while(y * y < limit ) : 
            n = (4 * x * x) + (y * y) 
            if (n <= limit and (n % 12 == 1 or n % 12 == 5)): 
                sieve[n] ^= True
            n = (3 * x * x) + (y * y) 
            if (n <= limit and n % 12 == 7): 
                sieve[n] ^= True
            n = (3 * x * x) - (y * y) 
            if (x > y and n <= limit and n % 12 == 11): 
                sieve[n] ^= True
            y += 1
        x += 1
      
    # Mark all multiples of squares as non-prime 
    r = 5
    while(r * r < limit) : 
        if (sieve[r]) : 
            for i in range(r * r, limit, r * r): 
                sieve[i] = False
          
    # Print primes using sieve[] 
    for a in range(5 , limit ): 
        if (sieve[a]): 
            print(a , end = " ") 
  
# Driver Code 
limit = 20
SieveOfAtkin(limit)
