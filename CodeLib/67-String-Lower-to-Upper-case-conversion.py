"""
Lower to upper case conversions
Tue, Apr 7, 2020
"""

s = input()

#method1: Using Ascii
for i in s:
    i = chr(ord(i)&~32)
    print(i)
    
#method2: Using string.lower() API
print(s.upper())
