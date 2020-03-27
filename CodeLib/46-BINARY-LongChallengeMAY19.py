T = int(input())
for iterations in range(T):
    N,Z = list(map(int,input().split(' ')))
    An = list(map(str,input().split(' ')))
    Bn = An[:]
    for j in range(Z):
        for i in range(N-1):
            if(An[i]=='0'):
                if(An[i+1]=='1'):
                    Bn[i] = '1'
                    Bn[i+1] = '0'
    Bn = " ".join(Bn)
    print(Bn)
