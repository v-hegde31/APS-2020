"""
Created on Wed Jan 15 09:38:55 2020
MARCHA1
"""
K = 20
index = [list(map(int,bin(i)[2:])) for i in range(2**K)]
for i in range(0,2**K):
        if len(index[i])<K:
            for j in range(K-len(index[i])):
                index[i].insert(0,0)

T = int(input())
for _ in range(T):
    (N,M) = list(map(int,input().split(" ")))
    notes = []
    for __ in range(N):
        notes.append(int(input()))
        
    for i in range(0,2**N):
        Sum = 0
        count = 0
        for j in range(K-N,K):
            if index[i][j] == 1:
                print(notes[count],Sum)
                Sum += notes[count]
            count += 1
        print('final',Sum)
        flag = 1
        if Sum == M:
            print("YES")
            flag = 0
            break
    if flag == 1:
        print("NO")
