def calc_max(result,n):
	for i in range(2,n+1):
		for j in range(1,i//2+1):
			result[i] = max(result[i],j*(i-j),j*(result[i-j]))
	return result
if __name__ == '__main__':
	n = int(input())
	result = [0 for i in range(n+1)]
	result = calc_max(result,n)
	print(result)
