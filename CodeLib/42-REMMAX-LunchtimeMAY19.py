T = int(input())
for i in range(T):
    count = 0
    num = list(map(int,input()))
    i=0
    if len(num)==1:
         s = map(str, num)   
         s = ''.join(s)         
         print(int(s))        
    elif num[0]==1:
        if len(num)>2:
            for i in range(2,len(num)):
                if num[i]==9:
                    count +=1
            if num[1]!=0 and count !=len(num)-2:
                num[1] -= 1 
                for i in range(2,len(num)):
                    num[i]=9
            else:
                i=1
                while(num[i]==0 and i<len(num)-1):
                    i+=1
                if i == len(num)-1:
                    if num[-1]==0:
                        num[0]=0
                        for i in range(1,len(num)):
                            num[i]=9
                else:
                    count = 0
                    for j in range(i+1,len(num)):
                        if num[j]==9:
                            count +=1                
                    if count != len(num)-1-i:
                        num[i]-=1
                        for j in range(i+1,len(num)):
                            num[j]=9   
        elif num[1]==0:
            num[0]=0
            num[1]=9
        s = map(str, num)   
        s = ''.join(s)         
        print(int(s))
    else:
        for i in range(1,len(num)):
            if num[i]==9:
                count +=1
        if count != len(num)-1:
            num[0]-=1
            for i in range(1,len(num)):
                num[i]=9
        s = map(str, num)   
        s = ''.join(s)         
        print(int(s))
