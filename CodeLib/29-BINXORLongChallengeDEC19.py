"""
Created on Sun Dec  8 09:06:01 2019
"""

def binaryToDecimal(binary): 
    decimal, i= 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

from itertools import permutations 

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(input())
    B = list(input())
    
    permA = permutations(A)
    permB = permutations(B)
    Alist = []
    Blist = []
    XORlist = []
    for i in list(permA): 
        l = "".join(i)
        k = binaryToDecimal(int(l))
        if k not in Alist: Alist.append(k)
        
    for i in list(permB): 
        j = "".join(i)
        k = binaryToDecimal(int(j))
        if k not in Blist: Blist.append(k)
    
    for i in range(len(Alist)):
        for j in range(len(Blist)):
            XORlist.append(Alist[i]^Blist[j])
    print(len(set(XORlist)))
    print(set(XORlist))
