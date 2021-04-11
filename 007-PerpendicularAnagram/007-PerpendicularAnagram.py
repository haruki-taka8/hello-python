# 007-PerpendicularAnagram.py
# > im useless
#             I   m useless
#         i   M    useless
#        im       useless
#       im    U   seless
#      im u   S   eless
#     im us   E   less
#    im use   L   ess
#   im usel   E   ss
#  im usele   S   s
# im useles   S

import math
inp = input('> ')
x = len(inp)

for i in range(x, 0, -1):
    sep = ' ' * math.floor(math.sqrt(x))
    toPrint = inp[:x-i] + sep + inp[x-i].capitalize() + sep + inp[x-i+1:]

    print(' '*i, toPrint)