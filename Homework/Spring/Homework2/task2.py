vis = set()


def dfs(v):
    if v in vis:
        return
    vis.add(v)
    if v not in d:
        return
    for i in d[v]:
        if i not in vis:
            dfs(i)


def fun(x, y):
    dfs(y)
    if x in vis:
        res.append("Yes")
    else:
        res.append("No")
d = {}
n = int(input())
for i in range(1, n+1):
    g = list(input().split(' '))
    if (g[0] not in d) and len(g) == 1:
        if len(g) == 1:
            d[g[0]] = []
    else:
        k = len(g)
        for j in g[2-k:]:
            if g[0] not in d:
                d[g[0]] = [j]
            else:
                d[g[0]].append(str(j))
q = int(input())
res = []
for i in range(1, q+1):
    s = list(input().split(' '))
    fun(s[0], s[1])
    vis = set()
for i in res:
    print(i)
