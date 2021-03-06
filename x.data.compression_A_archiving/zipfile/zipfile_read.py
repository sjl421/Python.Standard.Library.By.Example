#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Retrieve the contents of an archive member.
"""

import zipfile

with zipfile.ZipFile('example.zip') as zf:
    for filename in [ 'README.txt', 'notthere.txt' ]:
        try:
            data = zf.read(filename)
        except KeyError:
            print 'ERROR: Did not find %s in zip file' % filename
        else:
            print filename, ':'
            print data
        print
