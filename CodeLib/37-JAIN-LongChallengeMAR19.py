T = int(input())
vowel = [0,'a','e','i','o','u']
for iterations in range(T):
    N = int(input())
    count = 0
    one_list = []
    two_list = []
    three_list = []
    four_list = []
    five_list = []
    for i in range(N):
        temp = input()
        tempList = list(set(temp))
        vowelNum = []
        for j in range(len(tempList)):
            vowelNum.append(vowel.index(tempList[j]))
        if len(set(temp)) == 2:
            two_list.append(vowelNum)
            print(two_list)
        elif len(set(temp)) == 1:
            one_list.append(vowelNum)
        elif len(set(temp)) == 3:
            three_list.append(vowelNum)
        elif len(set(temp)) == 4:
            four_list.append(vowelNum)
        else:
            five_list.append(vowelNum)
    vowelindex = [1,2,3,4,5]
    if len(five_list) != 0:
        for i in range(1,len(five_list)+1):
            count = count + N - i
    if len(three_list) != 0:
        threeCompliment = []
        for i in range(len(three_list)):
            threeCompliment.append(list(set(vowelindex) - set(three_list[i])))
    if len(four_list) != 0:
        fourCompliment = []
        for i in range(len(four_list)):
            fourCompliment.append(list(set(vowelindex) - set(four_list[i])))
    print(count)
