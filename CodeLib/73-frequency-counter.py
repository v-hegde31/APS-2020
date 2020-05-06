S = "somesillystring"
freq = {}
for i in S:
  if i in freq:
    freq[i] += 1
  else:
    freq[i] = 1
print(freq)
