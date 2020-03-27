t = int(input())
for l in range(t):
    n,m=map(int,input().split(' '))
    arr=[[0 for i in range(m)] for j in range(n)]
    if n+m <= 3:
        k = 1
        arr=[[1 for i in range(m)] for j in range(n)]
    elif n == 2 and m == 2:
        k = 2
        arr=[[1,1],[2,2]]
    elif n == 1 or m == 1:
        k = 2
        for i in range(n):
                for j in range(m):
                    if n == 1:
                        arr[i][j] = ((j//2)%2)+1
                    else:
                        arr[i][j] = ((i//2)%2)+1
    elif n == 2 or m == 2:
        k = 3
        for i in range(n):
            for j in range(m):
                if n == 2:
                    arr[i][j] = (j%3)+1
                else:
                    arr[i][j] = (i%3)+1
    else:
        k = 4                
        for i in range(n):
            for j in range(m):
                if i%4 == 0 or i%4 == 1:
                    arr[i][j] = (j%4)+1
                else:
                    arr[i][j] = (j+3)%4
                    if(j+3)%4 == 0:
                        arr[i][j] = 4
    print(k)
    for i in range(n):
        temp = ' '.join(str(a) for a in arr[i])
        print(temp)
