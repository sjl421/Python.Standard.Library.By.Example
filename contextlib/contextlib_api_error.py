#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementing the context manager API by hand.
"""

class Context(object):
    def __init__(self, handle_error):
        print '__init__(%s)' % handle_error
        self.handle_error = handle_error
    def __enter__(self):
        print '__enter__()'
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__()'
        print '  exc_type =', exc_type
        print '  exc_val  =', exc_val
        print '  exc_tb   =', exc_tb
        return self.handle_error
        
with Context(True):
    raise RuntimeError('error message handled')

print

with Context(False):
    raise RuntimeError('error message propagated')
