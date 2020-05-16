S = input()

stack = []
for i in S:
    if i == '(':
        stack.append("$")
    elif i == ')':
        if stack:
            stack.pop()
        else:
            stack.append("$")
            break

if stack:
    print("Invalid Brace sequence")
else:
    print("Sequence Valid")
