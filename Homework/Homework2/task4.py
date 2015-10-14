def rpfilter(n, *a):
    def euclid(a, b):
        k = max(a, b)
        l = min(a, b)
        if k % l == 0:
            return l
        else:
            return euclid(l, k % l)
    b = []
    lst1 = []
    for i in a:
        i = int(i)
        b. append(i)
        if euclid(n, i) == 1:
                lst1.append(i)
    return lst1
a = input().split()
c = int(a[0])
lst2 = rpfilter(c, *a)
if len(lst2) == 0:
    print(None)
else:
    for z in lst2:
        print(z, '', end="")

