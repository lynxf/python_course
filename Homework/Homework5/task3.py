import re
import sys
data = sys.stdin.read()
data = data.split("\n")
c = 1
l = []
for i in data:
    k = re.findall("(\w+) = ", i)
    if len(k) != 0:
        print(c, k[0])
    c += 1 
