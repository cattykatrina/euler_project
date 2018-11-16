# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : 348.py
#
#* Purpose :
#
#* Creation Date : 11-11-2018
#
#* Last Modified : Friday 16 November 2018 10:07:43 PM IST
#
#* Created By :

#_._._._._._._._._._._._._._._._._._._._._.#
import math

import palindrome

def is_square(n):
    root = math.sqrt(n)
    if int(root+0.5) ** 2 == n:
        return True
    else:
        return False

def is_cube(n):
    root = n **(1/3)
    if int(root+0.5) ** 3 == n:
        return True
    else:
        return False

print(is_cube(27))
print(is_cube(20))
