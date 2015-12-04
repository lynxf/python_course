import sys
import re
data = sys.stdin.read()
results = re.findall("[Yy]+ou", data)
print(int(len(results)))
