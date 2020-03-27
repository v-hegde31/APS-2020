from itertools import combinations

T = int(input())
for _ in range(T):
    N,M = map(int,input().split(" "))
    X = list(map(int,input().split(" ")))
    Y = list(map(int,input().split(" ")))
    count = 0
    Xcomb = list(combinations(X,2))
    Ycomb = list(combinations(Y,2))
    Xfreq = {}
    Yfreq = {}
    for i in X:
        try:
            Xfreq[i**2]+=1
        except:
            Xfreq[i**2]=1
    for i in Y:
        try:
            Yfreq[i**2]+=1
        except:
            Yfreq[i**2]=1
    for i in Xcomb:
        if i[0]*i[1]<0:
            try:
                product = Yfreq[-1*i[0]*i[1]]
                count+=product
            except:
                continue
    if 0 in Xfreq:
        count+= (N-1)*M
        
    for i in Ycomb:
        if i[0]*i[1]<0:
            try:
                product = Xfreq[-1*i[0]*i[1]]
                count+=product
            except:
                continue
    if 0 in Yfreq:
        count+= (M-1)*N        
    print(count)
