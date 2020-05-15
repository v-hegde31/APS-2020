A = list(map(int,input().split(" ")))
k = A[0]
for i in range(1,len(A)):
    k = k^A[0]
#Since x^x = 0 and x^0 = x, the only number with no pair in the array is stored in k after the loop. 
print(k)
