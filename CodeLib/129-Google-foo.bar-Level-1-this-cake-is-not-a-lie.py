def solution(s):
    for i in range(1,len(s)):
        temp = s[:i]
        if temp*(len(s)//len(temp)) == s:
            return len(s)//len(temp)
    return 1
print(solution("vibha"))
