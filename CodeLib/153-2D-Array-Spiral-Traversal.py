def clockwise(A,N,M):
    k,l = 0,0
    while(k<M and l<N):
        for i in range(l,N):
            print(A[k][i], end = " ")
        k+=1
        
        for i in range(k,M):
            print(A[i][N-1], end = " ")
        N-=1
        if k<M:
            for i in range(N-1,l-1,-1):
                print(A[M-1][i], end = " ")
            M-=1
        if l<N:
            for i in range(M-1,k-1,-1):
                print(A[i][l], end = " ")
            l+=1
            
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int,input().split(" "))))
clockwise(A,N,N)
