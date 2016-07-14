#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementing the context manager API by hand.
"""

class Context(object):
    def __init__(self):
        print '__init__()'
    def __enter__(self):
        print '__enter__()'
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__()'
        
with Context():
    print 'Doing work in the context'
