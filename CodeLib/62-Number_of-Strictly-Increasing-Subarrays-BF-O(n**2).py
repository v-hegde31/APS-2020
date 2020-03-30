"""
March 20, 2020
Brute Force code for number of strictly increasing subarrays in a given Array. 
Time Complexity: O(n^2)
"""

def increasingSubArray(N,A):
    count = 0
    for i in range(N):
        for j in range(i+1,N):
          if A[j] > A[j-1]:
              count+=1
          else:
              break
    return count

if "__name__" == "__main__":
    N = int(input())
    A = list(map(int,input().split(" ")))
    increasingSubArray(N,A)
