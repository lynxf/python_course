import re
import requests
with open("e2.txt", "r") as d:
    l = d.read()
    l = l.split("\n")
    Lst = []
    d.close()
    for i in l:
        t = i
        response=requests.get(i)
        html_code=response.text
#print(html_code)
        regex='\w+@+\w+\.+\w+'
        results=re.findall(regex, html_code)
        Lst.append(results)
u = []
with open("bla-bla.txt", "w") as a:
    for i in Lst:
        for j in i:
            u.append(j)
    d={}
    for i in u:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for i in d:
        a.write(i)
        a.write('\n')
    a.close()
