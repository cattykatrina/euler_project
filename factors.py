# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : factors.py
#
#* Purpose :
#
#* Creation Date : 18-11-2018
#
#* Last Modified : Sunday 18 November 2018 11:58:13 AM IST
#
#* Created By :

#_._._._._._._._._._._._._._._._._._._._._.#
import math
from functools import lru_cache

@lru_cache(maxsize=None)
def additive_factors(n):
    for i in range(2, int(n/2)):
        yield i, n-i

@lru_cache(maxsize=None)
def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def multiplicative_factors(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            yield i


@lru_cache(maxsize=None)
def prime_factors(n):
    if is_prime(n):
        yield n
    for i in range(2, int(n/2)+1):
        if n % i == 0:
           if is_prime(i):
                yield i
