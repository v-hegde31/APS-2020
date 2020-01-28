"""
Dynamic Programming for Longest Subsequence Problem as taught in class.
January, 28th, 2020
"""
def commonSubseq(s1,s2):
    LCS = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
    return LCS

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    length = commonSubseq(s1,s2)
    for i in length:
        print(i)
