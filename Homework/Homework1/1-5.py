d = {}
s = str(input())
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in sorted(d):
    print (i, d[i])