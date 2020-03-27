def countSetBits_parity(n):
    parity=False
    while(n):
        parity=not parity
        n=n&(n-1)
    return parity

T = int(input())
for _ in range(T):
    N,Q = map(int,input().split(" "))
    A = list(map(int,input().split(" ")))
    even,odd=0,0
    for i in A:
        if(countSetBits_parity(i)):
            odd+=1
        else:
            even+=1
    for __ in range(Q):
        P = int(input())
        if(countSetBits_parity(P)):
            print(odd,even)
        else:
            print(even,odd)
        
