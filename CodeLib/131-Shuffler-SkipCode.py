S = list(input().split(" "))
Skip = []
for i in S:
    t = len(i)
    if t>3:
        count,j,k = 0,0,t//2
        temp = ""
        while count<(t//2)*2:
            if count%2==0:
                temp+=i[j]
                j+=1
                count+=1
            else:
                temp+=i[k]
                k+=1
                count+=1
        if t%2==1:
            temp+=i[t-1]
        Skip.append(temp)
    else:
        Skip.append(i)
print(" ".join(Skip))
