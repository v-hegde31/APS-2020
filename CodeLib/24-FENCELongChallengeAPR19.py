T = int(input())
for iterations in range(T):
    N,M,K = list(map(int,input().split(" ")))
    a = []
    index = []
    count = 0
    a = [0] * (M+2) * (N+2)
    for i in range(K):
        r,c = list(map(int,input().split(" ")))
        a[r*(M+2) + c] = 1
        index.append((r,c))
    for i in range(K):
        x,y = index[i][0],index[i][1]
        if a[x*(M+2) + y + 1] == 0:
            count+=1
        if a[x*(M+2) + y - 1] == 0:
            count+=1
        if a[(x-1)*(M+2) + y] == 0:
            count+=1
        if a[(x+1)*(M+2) + y] == 0:
            count+=1
    print(count)
