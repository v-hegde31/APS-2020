T = int(input())
for _ in range(1,T+1):
    N,K = map(int,input().split(" "))
    A = input()
    K_list= [str(i) for i in range(K,0,-1)]
    K_string = " ".join(K_list)
    
    print('Case #'+str(_)+':',A.count(K_string))
