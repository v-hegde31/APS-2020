"""
Created on Sat May  9 19:32:01 2020
Caesar Cipher - Encoder + Decoder
"""
def encode(data,key):
    new_data = []
    for i in data:
        x = ord(i)
        if (x>= 97 and x<=122) or (x>=65 and x<=90):
            x+=(key%26)
            if x>122 or (i.isupper() and x>90):
                x-=26
        new_data.append(chr(x))
    print("".join(new_data))

def decode(data,key):
    new_data = []
    for i in data:
        x = ord(i)
        if i.isalpha():
            x-=(key%26)
            if (i.islower() and x<97) or x<65:
                x+=26
        new_data.append(chr(x))
    print("".join(new_data))    
            
print("MENU")
print("1. Encode Message")
print("2. Decode Message")
print("Input choice and text data")
option, data = list(input().split(" "))
option = int(option)
print("Input Key")
key = int(input())

if option == 1:
    encode(data,key)
elif option == 2:
    decode(data,key)
else:
    print("Error!")
