#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Writing to a memory mapped file using a slice assignment.

"""

import mmap
import shutil
import contextlib

# Copy the example file
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = 'consectetuer'
reversed = word[::-1]
print 'Looking for    :', word
print 'Replacing with :', reversed

with open('lorem_copy.txt', 'r+') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0)) as m:
        print 'Before:'
        print m.readline().rstrip()
        m.seek(0) # rewind

        loc = m.find(word)
        m[loc:loc+len(word)] = reversed
        m.flush()

        m.seek(0) # rewind
        print 'After :'
        print m.readline().rstrip()

        f.seek(0) # rewind
        print 'File  :'
        print f.readline().rstrip()
