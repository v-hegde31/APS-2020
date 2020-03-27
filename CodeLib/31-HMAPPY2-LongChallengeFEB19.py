import math
t = int(input())
for i in range(0,t):
    temp = list(map(int,input().split(' ')))
    (N,a,b,k) = (temp[0],temp[1],temp[2],temp[3])
    acount = N//a
    bcount = N//b
    lcmcount = N//(a*b//math.gcd(a,b))
    kcompute = acount+bcount - 2*lcmcount
    if kcompute < k:
        print('Lose')
    else:
        print('Win')
