with open("name", "r") as d:
    l = d.read()
    l = l.split("\n")
    w_yo = 0
    w_ka = 0
    w_v = 0
    for i in l:
        if "yo" == (i[-2]+i[-1]):
            w_yo += 1
        elif "ka" == (i[-2]+i[-1]):
            w_ka += 1
        else:
            w_v += 1
    d.close()

    def fac(n):
        if n == 0:
            return 1
        return fac(n-1) * n

    if w_yo < 7:
        numb_yo = w_yo
    else:
        numb_yo = 7

    comb_yo = 0
    for i in range(0, numb_yo):
        comb_yo += fac(w_yo)//fac(i)
    best = comb_yo * w_ka * w_v
    print(best)
