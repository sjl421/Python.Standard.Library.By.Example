#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Handling recursive data structures.

"""

from pprint import pprint

local_data = [ 'a', 'b', 1, 2 ]
local_data.append(local_data)

print 'id(local_data) =>', id(local_data)
pprint(local_data)
