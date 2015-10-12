str = input().split()
a = int(str[0])
b = int(str[1])


def euclid(a, b):
    k = max(a, b)
    l = min(a, b)
    if k % l == 0:
        return l
    else:
        return euclid(l, k % l)
print(euclid(a, b))
