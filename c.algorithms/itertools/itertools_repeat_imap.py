#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using repeat() and imap()

"""

from itertools import *

for i in imap(lambda x,y:(x, y, x*y), repeat(2), xrange(5)):
    print '%d * %d = %d' % i
