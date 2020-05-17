def getMinVal(total_lambs):
    n, sum, count = 1, 1, 1
    while True:
        n*=2
        sum += n
        if sum > total_lambs:
            break
        count+=1
    return count

def getMaxVal(total_lambs):
    if total_lambs == 1:
        return 1
    if total_lambs == 2:
        return 2
    f0,f1,sum,count=1,1,2,2
    while True:
        f2 = f1 + f0
        sum += f2
        if sum > total_lambs:
            break
        f0 = f1
        f1 = f2
        count += 1
    return count

def solution(total_lambs):
    min_val = getMinVal(total_lambs)
    max_val = getMaxVal(total_lambs)
    return max_val - min_val
