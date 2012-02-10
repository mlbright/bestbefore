#!/usr/bin/python

import sys
import re
import datetime
import itertools

def solve(date_str):
    parts = map(int,date_str.split('/'))
    attempts = sorted(itertools.permutations(parts))
    for dt in attempts:
        year = dt[0] + 2000 if dt[0] < 1000 else dt[0]
        try:
            print datetime.date(year,dt[1],dt[2]).strftime("%Y-%m-%d")
            return
        except ValueError:
            pass
    print "%s is illegal" % (date_str)
    
    
if __name__ == "__main__":
    solve(sys.stdin.readline().strip())
