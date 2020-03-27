# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:30:26 2019
Euler #9 - Pythagorean Triple such that a+b+c = 1000
@author: Vibha
"""
def pythagoreanTriplets(limits) : 
    c, m = 0, 2
    while c < limits :  
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n
            if c > limits : 
                break
  
            print(a,b,c,a+b+c,a*b*c)
  
        m = m + 1
  
  
# Driver Code 
if __name__ == '__main__' : 
      
    limit = 19
    pythagoreanTriplets(limit)
    
#40 is the only number divisible by 1000. 1000/40 = 25. so multiply each of a,b,c by 25 and then multiply a,b,c.
#same as abc*25^3 where a+b+c = 40
    
