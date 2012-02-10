#!/usr/bin/python

import sys
import re
from datetime import datetime
from itertools import permutations

def illegal(s):
    print "%s is illegal" % (s)
    sys.exit()

def solve(date_str):
    millenium = datetime(2000,1,1)
    sanitized = []
    for part in date_str.split('/'):
        tmp = re.sub(r'^00?$','2000',part)
        sanitized.append(tmp)
    date_str = '/'.join(sanitized)
    perms = list(permutations(['%Y','%m','%d'],3))
    perms.extend(list(permutations(['%y','%m','%d'],3)))
    formats = [ '/'.join(p) for p in perms ]
    dates_ = []
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str,fmt)
        except:
            continue
        dates_.append(dt)
    dates_.sort()
    if not dates_:
        illegal(date_str)
    if dates_[0] < millenium:
        illegal(date_str)
    print dates_[0].strftime("%Y-%m-%d")
    
if __name__ == "__main__":
    solve(sys.stdin.readline().strip())
