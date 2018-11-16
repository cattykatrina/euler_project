# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : 348.py
#
#* Purpose :
#
#* Creation Date : 11-11-2018
#
#* Last Modified : Friday 16 November 2018 11:21:44 PM IST
#
#* Created By :

#_._._._._._._._._._._._._._._._._._._._._.#
import math

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

def candidate(n):
    ways = list()
    for i,j in additive_factors(n):
        if len(ways) > 4:
            return False
        if is_cube(j):
            if is_square(i):
                ways.append((i,j))
                print(n, i,j)
        elif is_square(j):
            if is_cube(i):
                ways.append((i,j))
                print(n, i,j)
    if len(ways) == 4:
        return True
    return False

def main():
    res = list()
    i=1
    while len(res) <5:
        palind = palindrome(i)
        print(palind)
        right_no = candidate(palind)
        if right_no:
            res.append(palind)
        i = i+1
    print(res)
    print(sum(res))

main()
