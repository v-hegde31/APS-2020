"""
Created on Mon Nov 12 07:05:47 2018
"""
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print("Enter a string")
s = input()
print(char_frequency(s))
