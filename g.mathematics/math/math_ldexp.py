#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""From mantissa, exponent pair to floating point value.
"""

import math

print '{:^7}  {:^7}  {:^7}'.format('m', 'e', 'x')
print '{:-^7}  {:-^7}  {:-^7}'.format('', '', '')

for m, e in [ (0.8, -3),
              (0.5,  0),
              (0.5,  3),
              ]:
    x = math.ldexp(m, e)
    print '{:7.2f}  {:7d}  {:7.2f}'.format(m, e, x)
