a = [int(s) for s in input().split()]
h=len(a)
p=[]
k=a[0:h:2]
l=a[1:h:2]
w=len(l)
x=1
while x!=w+1:
    i=min(k)
    t=k.index(i)
    p.append(i)
    del k[t]
    j=max(l)
    m=l.index(j)
    p.append(j)
    del l[m]
    x+=1
for z in p:
    print(z, '', end="")