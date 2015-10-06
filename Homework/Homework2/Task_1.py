def combinations(n, k):
    def fac(a):
        p = 1
        for i in range(1, a + 1):
            p *= i
        return p
    if k > n:
        return 0
    elif k == n or k == 0:
        return 1
    else:
        return fac(n)/(fac(k)*fac(n-k))
n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
print(int(combinations(n, k)))
