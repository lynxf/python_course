import sys
import re
data = sys.stdin.read()
results = re.findall("you", data)
print(int(len(results)))
