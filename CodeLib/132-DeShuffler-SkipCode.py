S = list(input().split(" "))
Skip = []
for i in S:
    t = len(i)
    if t>3:
        temp = ""
        for j in range(0,t-1,2):
            temp+=i[j]
        for j in range(1,t,2):
            temp+=i[j]
        if t%2==1:
            temp+=i[t-1]
        Skip.append(temp)
    else:
        Skip.append(i)
print(" ".join(Skip))
