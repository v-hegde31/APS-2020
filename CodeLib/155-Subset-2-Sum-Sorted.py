"""
For better space complexity than Hashmap, A sorted array is used and two pointers are manipulated to find the solution.
If sum is greater than given sum, the left pointer is moved right, else the right pointer is moved left to find the optimal subset of length 2 that has given sum.

Space Complexity: O(1)
Time Complexity:  O(nlogn)        [Depends on the sorting algorithm.]
"""

T = int(input())
for _ in range(T):
    A = list(map(int,input().split(" ")))
    S = int(input())
    A.sort()
    L,R = 0, len(A)-1
    while A[L]+A[R] != S and L<R:
        if A[L]+A[R]>S:
            R-=1
        else:
            L+=1
    if L==R:
        print("No Soln")
    else:
        print(A[L],A[R])
