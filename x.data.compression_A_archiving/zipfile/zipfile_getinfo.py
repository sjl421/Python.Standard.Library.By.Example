#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Retrieve all of the metadata for one member of an archive.
"""

import zipfile

with zipfile.ZipFile('example.zip') as zf:
    for filename in [ 'README.txt', 'notthere.txt' ]:
        try:
            info = zf.getinfo(filename)
        except KeyError:
            print 'ERROR: Did not find %s in zip file' % filename
        else:
            print '%s is %d bytes' % (info.filename, info.file_size)
