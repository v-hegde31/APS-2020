"""
Critical Number Identification - Squareroot Decomposition
For naive intuition. 
"""
from random import randint
from math import sqrt

N = int(input())
critical = randint(1,N)
print("Critical Number is determined.")
print("")

block = int(sqrt(N))
print("Block Size = ",block)
print("")
x = 0
while x<critical:
    x+=block
    print("The Critical Number is greater than ",x-block)
x-=block
    
print("")
print("Critical Block is determined.")
print("Critical block:",x,"-",x+block)
print("")

for i in range(x,x+block):
    if i == critical:
        print("Critical Number Found")
        print("Critical Number Under N =",N,"=",i)
