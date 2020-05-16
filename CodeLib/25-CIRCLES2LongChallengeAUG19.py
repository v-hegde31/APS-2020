"""
Created on Sun Aug 18 21:36:30 2019
Cook Off Aug 19 - CIRCLES2
"""

def circle(x1, y1, x2,y2, r1, r2): 
    distSq = (((x1 - x2)* (x1 - x2))+ ((y1 - y2)* (y1 - y2)))**(.5) 
    if (distSq + r1 <= r2): 
        print("NO") 
    else: 
        print("YES") 

T = int(input())
for _ in range(T):
    (x1,y1,x2,y2,r1,r2) = list(map(int,input().split(' ')))
    
    circle(x1, y1, x2, y2, r1, r2)
