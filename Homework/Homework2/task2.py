def prime(n):
    i = 2
    j = 0
    while i**2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    else:
        return True
a = []
for i in range(int(input())):
        a.append(int(input()))
list_TF = []
for i in a:
    t = prime(i)
    list_TF.append(t)
for i in list_TF:
    print(i)
