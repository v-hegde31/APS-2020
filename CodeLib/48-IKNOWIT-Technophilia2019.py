"""
Created on Fri Mar 29 15:10:21 2019
"""

t=int(input())
for testcase in range(t):
    s="I know "
    a="that I forgot "
    b="that I know "
    n=int(input())
    for i in range(n,1,-1):
        if n%2 == 1:
            if i%2==0:
                s+=b
            else:
                s+=a
        else:
            if i%2==0:
                s+=a
            else:
                s+=b
    s+="it"
    print(s)
