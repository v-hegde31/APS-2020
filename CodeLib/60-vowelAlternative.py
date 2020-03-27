def vowel_count(s, vowels): 
    count = {}.fromkeys(s, 0) 
    for i in range(len(s)):
        s[i] = s[i].casefold()
        
        for j in s[i]: 
            if j in vowels: 
                count[j] += 1	
    return count 
	
vowels = 'aeiou'
s = input()
k = s.split(" ")
print(k)
s = ("").join(k)
if(len(s)==0):
    print("Empty String")
elif(s.isalpha()==False):
    print("Given input has digits or special characters. Please give valid input")
else:
    print (vowel_count(k, vowels))
