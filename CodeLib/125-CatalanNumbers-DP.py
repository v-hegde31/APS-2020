def cat(n):
    catalan=[0]*(n)
    catalan[0],catalan[1],catalan[2]=1,1,2
    
    for i in range(3,n):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[(i-1)-j]
    
    return catalan

n=20
print(*cat(n))
