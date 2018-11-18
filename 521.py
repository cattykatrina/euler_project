# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : 521.py
#
#* Purpose :
#
#* Creation Date : 18-11-2018
#
#* Last Modified : Sunday 18 November 2018 12:00:58 PM IST
#
#* Created By :

#_._._._._._._._._._._._._._._._._._._._._.#

import factors

def main(n):
    res = list()
    for i in range(2, n):
        res.append(min(factors.prime_factors(i)))
    return res

s_smpf = sum(main(10**12))
print(s_smpf % 10**9)


