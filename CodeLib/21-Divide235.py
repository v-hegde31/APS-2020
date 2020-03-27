"""
Jun 24, 2019
CodeForces 1176A
"""
t=int(input())
for _ in range(t):
    n=int(input())
    original=n
    count=0
    while(n!=1):
        if n%5==0:
            n=(4*n)//5
        elif n%3==0:
            n=(2*n)//3
        elif n%2==0:
            n=n//2
        else:
            count=-1
            break
        count+=1
    print(count)
