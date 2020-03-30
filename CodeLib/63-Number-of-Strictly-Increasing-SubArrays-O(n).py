"""
March 30, 2020
Optimised code to count the number of subarrays in a given Array.
Time Complexity: O(n)
"""
def increasingSubArray(N,A):
    count = N
    length = 1
    for i in range(N-1):
        if A[i+1]>A[i]:
            length+=1
        else:
            len = 1
            count += (((length-1)*length)//2)
    if len>1:
        count += (((length-1)*length)//2)
    break

if "__name__" == "__main__":
    N = int(input())
    A = list(map(int,input().split(" ")))
    print(increasingSubArray(N,A))
