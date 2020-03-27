"""
26 Jan,2020
Dynamic Programming for Stable Marriage Problem
"""
linp = lambda a:list(map(int,input().split(' ')))
minp = lambda a:map(int,input().split(' '))
inp = lambda a:int(input())
MD=1000000007

N=int(input())
proposal_count=[0]*N

def wPrefersM1OverM(prefer, w, m, m1):
    global N
    for i in range(N):
        if (prefer[w][i] == m1):
            return True
        if (prefer[w][i] == m):
            return False
def stableMarriage(prefer):
    global N
    global proposal_count
    wPartner = [-1 for i in range(N)]
    mFree = [False for i in range(N)]
    freeCount = N
    while (freeCount > 0):
        m = 0
        while (m < N):
            if (mFree[m] == False):
                break
            m += 1
        i = 0
        while i < N and mFree[m] == False:
            w = prefer[m][i]
            proposal_count[w]+=1
            if (wPartner[w - N] == -1):
                wPartner[w - N] = m
                mFree[m] = True
            freeCount -= 1
			else:
                m1 = wPartner[w - N] 
				if (wPrefersM1OverM(prefer, w, m, m1) == False):
                    wPartner[w - N] = m 
					mFree[m] = True
					mFree[m1] = False
			i += 1
	print("Woman ", " Man") 
	for i in range(N): 
		print(i + N, "\t", wPartner[i]) 

prefer=[]
m1,w1=[],[]
for i in range(N):
    m1.append(list(map(int,input().split(' '))))
for i in range(N):
    w1.append(list(map(int,input().split(' '))))

m_pref=[[0]*N for i in range(n)]
w_pref=[[0]*N for i in range(n)]
for i in range(N):
    for j in range(N):
        m_pref[i][m1[i][j]-1]=j
        w_pref[i][w1[i][j]-1]=j
        
for i in range(N):
    for j in range(N):
        m_pref[i][j]+=N
for i in m_pref:
    prefer.append(i)
for i in w_pref:
    prefer.append(i)

stableMarriage(prefer) 
print(proposal_count)

Q=int(input())
for q in range(Q):
    q1=int(input())
    print(proposal_count[q1-1])
