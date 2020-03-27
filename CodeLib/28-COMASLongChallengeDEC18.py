T = int(input())
for i in range(0,T):
    N = int(input())
    meat_list = []
    k_list = []
    t = 1
    while t != N+1:
        meat_list.append(t)
        k_list.append(t)
        t+=1
    k = N//5
    for l in range (0,k):
        m = 5*l
        print("?",m+1,m+2,m+3,m+4,m+5,flush = True)
        a,b = map(int,input().split(" "))
        meat_list.remove(a)
        meat_list.remove(b)
    k = len(meat_list)//5
    while k != 0:
        print("?",meat_list[0],meat_list[1],meat_list[2],meat_list[3],meat_list[4],flush = True)
        a,b = map(int,input().split(" "))
        meat_list.remove(a)
        meat_list.remove(b)
        k = len(meat_list)//5
    if len(meat_list) == 4:
        print("?",meat_list[0],meat_list[1],meat_list[2],meat_list[3],b,flush = True)
        a,b = map(int,input().split(" "))
        if (a in meat_list) == True:
            meat_list.remove(a)
            
        else:
            meat_list.remove(b)
    (a,b,c) = (meat_list[0],meat_list[1],meat_list[2])
    p = set(k_list)
    q = set(meat_list)
    r = p - q
    m = list(r)
    (x,y,z) = (m[0],m[1],m[2])
    print("?",a,b,x,y,z,flush = True)
    e,f = map(int,input().split(" "))
    print("?",c,b,x,y,z,flush = True)
    g,h = map(int,input().split(" "))
    print("?",a,c,x,y,z,flush = True)
    i,j = map(int,input().split(" "))
    if e == g and f == h:
        print("!",b,flush = True)
    elif g == i and h == j:
        print("!",c,flush = True)
    else:
        print("!",a,flush = True)
