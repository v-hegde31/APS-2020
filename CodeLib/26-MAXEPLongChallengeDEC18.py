import math
temp=list(map(int,input().split(' ')))
(N,c)=(temp[0],temp[1])
coins = 999
count = math.ceil((-1+math.sqrt(1+8*N))/2)
y = count
x = 1
repair = 2
print(x,y,flush=True)
result = int(input())
while result == 0 and y<N-(count):
    if(coins == 0):
        result = -1
    else:
        count-=1
        y+=count
        print(x,y,flush=True)
        coins-=1
        result = int(input())
if y>N:
    count +=1
    y-=count
    coins+=1
jelif (result == 1):
    print(repair,flush=True)
    coins-=c
    y-=count
result = 0
while (result == 0 and y != N):
    if(coins == 0):
        result = -1
    else:
        y+=1
        coins-=1
        print(x,y,flush=True)
        result = int(input())
if (result == 1):
    print(repair,flush=True)
    coins-=c
    x = 3
    print(x,y,flush=True)
elif(y==N):
    x = 3
    print(x,y,flush=True)
