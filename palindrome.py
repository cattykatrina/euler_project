# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* file name : palindrome.py
#
#* purpose :
#
#* creation date : 11-11-2018
#
#* last modified : saturday 17 november 2018 02:01:52 pm ist
#
#* created by :

#_._._._._._._._._._._._._._._._._._._._._.#
from functools import lru_cache

def is_palindrome(num_str):
    reversed_str = ''.join([c for c in reversed(num_str)])
    return bool(int(num_str) == int(reversed_str))

@lru_cache(maxsize=none)
def palindrome(n):
    cnt=0
    i =10
    while cnt!= n:
        if is_palindrome(str(i)):
            cnt = cnt+1
        i = i+1
    return i - 1


