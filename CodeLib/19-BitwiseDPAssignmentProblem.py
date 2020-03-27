"""
22 Feb, 2020

There are N persons and  tasks, each task is to be alloted to a single person. We are also given a matrix cost of size NxN,
where cost[i][j] denotes, how much person i is going to charge for task . 
Now we need to assign each task to a person in such a way that the total cost is minimum. 
Note that each task is to be alloted to a single person, and each person will be alloted only one task.
"""
def optimalSum(cost,n):
    dp = [float('inf') for i in range(2**n)]
    dp[0] = 0
    for mask in range(2**n):    
        x = sum(list(map(int,bin(mask)[2:])))
        for j in range(n):
            if mask & (1<<j) == 0:
                dp[mask|(1<<j)] = min(dp[mask|(1<<j)],dp[mask]+cost[x][j])
    return dp
        
if __name__ == "__main__":
    n = int(input())
    cost = []
    for i in range(n):
        cost.append(list(map(int,input().split(" "))))
    print(optimalSum(cost,n))
