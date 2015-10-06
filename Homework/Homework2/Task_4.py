def rpfilter(n):
    b = []
    for i in a:
        b.append(int(i))
    lst = b[1:]
    s = b[0]
    lst1 = []

    def euclid(a, b):
        k = max(a, b)
        l = min(a, b)
        if k % l == 0:
            return l
        else:
            return euclid(l, k % l)
    for i in lst:
            if euclid(s, i) == 1:
                lst1.append(i)
    return lst1
a = input().split()
lst2 = rpfilter(a)
if len(lst2) == 0:
    print(None)
else:
    for z in lst2:
        print(z, '', end="")

