#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The paths for a scheme.
"""

import sysconfig
import pprint

for scheme in ['posix_prefix', 'posix_user']:
    print scheme
    print '=' * len(scheme)
    print 'purelib =', sysconfig.get_path(name='purelib',
                                          scheme=scheme)
    print
