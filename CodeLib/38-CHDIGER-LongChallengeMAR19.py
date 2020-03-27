T = int(input())
glob_arr = [0,1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111,11111111111,111111111111,1111111111111,11111111111111,111111111111111,1111111111111111,11111111111111111,111111111111111111]

for iterable in range(T):
    (N,d) = map(int, input().split(" "))
    n = N
    K = []
    L = []
    I = []
    J = []
    
    K=[int(x) for x in str(N)]
    K.append(d)
    M = K[:]
    count = len(K) - 1
    L = K[:]
    L.sort()
    if min(K) >= d:
        print(d*glob_arr[count])
    elif max(K) < d and L == K:
        print(N)
    else:
        for i in range(count):
            if L[i] != -1:
                I.append(K.index(L[i]))
                K[K.index(L[i])] = -1
            else:
                continue
        m = I[0]
        j = 0
        for i in range(1,len(I)):
            i = i - j
            if I[i]<I[i-1]:
                j+=1
                I.pop(i)
        for i in range(len(I)):
            J.append(M[I[i]])
        v = count - len(I) + 1
        for i in range(v):
            J.append(d)
        final=[str(J[i]) for i in range(count)]
        res=''.join(final)
        print(res)
