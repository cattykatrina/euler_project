# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : 348.py
#
#* Purpose :
#
#* Creation Date : 11-11-2018
#
#* Last Modified : Saturday 17 November 2018 06:24:27 PM IST
#
#* Created By :

#_._._._._._._._._._._._._._._._._._._._._.#
import math
from functools import lru_cache

from palindrome import palindrome

def is_square(n):
    root = math.sqrt(n)
    if int(root+0.5) ** 2 == n:
        return True
    else:
        return False

def is_cube(n):
    root = n **(1/3)
    # A little unsure about this reasoning but let's just try
    if int(root+0.5) ** 3 == n:
        return True
    else:
        return False

def additive_factors(n):
    for i in range(2, int(n/2)):
        yield i, n-i

@lru_cache(max=None)
def candidate(n):
    ways = list()
    for i,j in additive_factors(n):
        if is_cube(j):
            if is_square(i):
                ways.append((i,j))
        elif is_square(j):
            if is_cube(i):
                ways.append((i,j))
        if len(ways) > 4:
            return False
    if len(ways) == 4:
        print(n, ways)
        return True
    return False

def search(start, end):
    res = list()
    i=1
    chosen = dict()
    #while len(res) <5:
    for i in range(1, 50000):
        palind = palindrome(i)
        right_no = candidate(palind)
        if right_no:
            chosen[i] = palind
            res.append(palind)
            print(chosen)
        i = i+1
    print(sum(res))
    return chosen

def main():
    give_up = 100000000000
    step = 50000
    for i in range(1, step):
    while i < give_up:
        res=search(i, i + step)
    print(res)
    main()
