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

for i in range(len(inp), 0, -1):
    toPrint = inp
    sep = ' ' * math.floor(math.sqrt(len(inp)))
    toPrint = toPrint[:len(inp)-i] + sep + toPrint[len(inp)-i].capitalize() + sep + toPrint[len(inp)-i+1:]

    print(' '*(i-1), end='')
    print(toPrint)