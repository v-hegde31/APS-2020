"""
Find sum of digits in a number recursively
"""

def digitSum(n):
    if n//10==0:
        return n
    else:
        return (n%10)+digitSum(n//10)

if __name__ == "__main__":
    print(digitSum(12345))
    print(digitSum(1931))
