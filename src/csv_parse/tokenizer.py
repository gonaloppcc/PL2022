import sys
import re

p = re.compile(r'\b([^\W\d]\w*)(?:/(\w+))?\b')

for line in sys.stdin:
    mo = p.findall(line)
    print(mo)