import math
def comb(n, r): 
	p = 1
	k = 1
	if (n - r < r): 
		r = n - r 
	if (r != 0): 
		while (r): 
			p *= n 
			k *= r 
			m = math.gcd(p, k) 
			p //= m 
			k //= m 
			n -= 1
			r -= 1
	else: 
		p = 1
	return p

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split(" ")))
    Q = int(input())
    for i_ in range(Q):
        L,R = map(int,input().split(" "))
        freq = {}
        count = 0
        for item in range(L-1,R): 
            if (A[item] in freq): 
                freq[A[item]] += 1
            else: 
                freq[A[item]] = 1
        nimheap = list(freq.values())
        xor = 0
        for i in nimheap:
            xor = xor^i
        if xor == 0:
            print("0")
            continue
        for i in nimheap:
            if xor ^ i < i:
                count += comb(i,xor^i)
        print(count%998244353)
