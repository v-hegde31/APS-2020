"""
Created on Mon Nov 19 08:25:12 2018
"""

def vowels_count(s):
    clist = []
    clist.append(["a",s.count("a")])
    clist.append(["e",s.count("e")])
    clist.append(["i",s.count("i")])
    clist.append(["o",s.count("o")])
    clist.append(["u",s.count("u")])
    return clist

s = input()
if(len(s)==0):
    print("Empty String")
elif(s.isalpha()==False):
    print("Given input has digits or special characters. Please give valid input")
else:
    t = list(s)
    print(vowels_count(t))
    
