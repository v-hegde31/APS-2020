n=int(input())
p=input()
q=input()
pd={i:0 for i in p}
qd={i:0 for i in q}
for i in p:
    pd[i]+=1
for i in q:
    qd[i]+=1
plst=list(zip(pd.keys(),pd.values()))
qlst=list(zip(qd.keys(),qd.values()))
for i in range(len(plst)):
    plst[i]=list(plst[i])
for i in range(len(qlst)):
    qlst[i]=list(qlst[i])
count=0
for i in range(len(plst)):
    for j in range(len(qlst)):
        if plst[i][0]==qlst[j][0] and plst[i][0]!='?' and qlst[j][0]!='?':
            count+=min(plst[i][1],qlst[j][1])
            if plst[i][1]==min(plst[i][1],qlst[j][1]):
                qlst[j][1] -= plst[i][1]
                plst[i][1]=0
            else:
                plst[i][1] -= qlst[j][1]
                qlst[j][1]=0
try:
    pq = pd['?']
except:
    pq=0
try:
    qq = qd['?']
except:
    qq=0
if qq==0 and pq!=0:
    count+=pq
elif pq==0 and qq!=0:
    count+=qq
else:
    (remp,remq)=(0,0)
    for i in range(len(plst)):
        if plst[i][0]=='?':
            continue
        remp+=plst[i][1]
    for i in range(len(qlst)):
        if qlst[i][0]=='?':
            continue
        remq+=qlst[i][1]
    if remp>0:
        count+=min(qq,remp)
        if qq==min(qq,remp):
            remp-=qq
        else:
            qq-=remp
    if remq>0:
        count+=min(pq,remq)
        if qq==min(pq,remq):
            remq-=pq
        else:
            pq-=remq
    count+=min(pq,qq)
print(count)
