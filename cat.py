import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"cat.*cat", line):
        print(line)
