"""
Created on Sat Dec 22 20:41:11 2018
To decode an ASCII sequence given in any base to a string. 
"""

t = list(map(int,input().split(' ')))
n = int(input())
u = len(t)
v = []
for i in range(u):
    count = 0
    s = 0
    while t[i] !=0:
        k = (t[i]%10)*(n**count)
        count+=1
        s = s+k
        t[i] = t[i]//10
    v.append(chr(s))

k = "".join(v)
print(k)
