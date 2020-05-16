def euclid_gcd(a, b):
  if a == 0:
    return b
  return euclid_gcd(b%a, a)

a, b = map(int,input().split(' '))
print(euclid_gcd(a,b))
