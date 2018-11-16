# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : palindrome.py
#
#* Purpose :
#
#* Creation Date : 11-11-2018
#
#* Last Modified : Friday 16 November 2018 10:03:44 PM IST
#
#* Created By :

#_._._._._._._._._._._._._._._._._._._._._.#
from functools import lru_cache

def is_palindrome(num_str):
    reversed_str = ''.join([c for c in reversed(num_str)])
    return bool(int(num_str) == int(reversed_str))

@lru_cache(maxsize=None)
def palindrome(n):
    cnt=0
    i =10
    while cnt!= n:
        if is_palindrome(str(i)):
            cnt = cnt+1
        i = i+1
    return i - 1


print(palindrome(300))
