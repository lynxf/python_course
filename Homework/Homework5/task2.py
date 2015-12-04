import sys
import re
data = sys.stdin.read()
data = data.split("\n")
t = []
for i in data:
    r = re.findall("0{3}|1{3}|2{3}|3{3}|4{3}|5{3}|6{3}|7{3}|8{3}|9{3}", i)
    if len(r) != 0:
        t.append(i)
for i in t:
    print(i)
