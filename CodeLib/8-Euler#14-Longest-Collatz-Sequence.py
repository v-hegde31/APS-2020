"""
Created on Sun Jun 23 02:27:32 2019
Brute Force code to find the longest collatz sequence under 1000000
"""
n = 10

def collatz(n):
    count = 0
    while n!=1:
        if n%2==0:
            n = n//2
        else:
            n = 3*n + 1
        count+=1
    return count

clist = []
for i in range(1,1000001):
    clist.append(collatz(i))
    
print(max(clist))
print(clist.index(max(clist)))
