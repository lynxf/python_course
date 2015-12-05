import re
with open("hp5.txt", "r") as d:
    l = d.read()
    l = l.split("\n")
    pat1 = '[A-Z][a-z]+ whispered| [A-Z][a-z]+ [A-Z][a-z]+ whispered|whispered+ [A-Z][a-z] |whispered+ [A-Z][a-z]+ [A-Z][a-z]| to whisper+ [A-Z][a-z]+ [A-z][a-z]|  to whisper+ [A-Z][a-z]|  to whisper+ [A-Z][a-z]+ [A-z][a-z]| [A-Z][a-z]+ [A-z][a-z]+ to whisper| [A-Z][a-z]+ to whisper' #| whispered +[A-Z][a-z]+ [A-z][a-z]| [A-Z][a-z]+ [A-z][a-z]+ to whisper | to whisper+ [A-Z][a-z]+ [A-z][a-z])'
    Lst = []
    for i in l:
        t = re.findall(pat1, i)
        if len(t) != 0:
            t = str(t)
            r = re.sub('(whispered|to whisrered|\W+)', " ", t)
            Lst.append(r)
d = {}
for i in Lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in sorted(d):
    print(i, d[i])
