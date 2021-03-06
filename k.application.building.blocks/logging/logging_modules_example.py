#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simulate logging from different modules

See http://blog.doughellmann.com/2007/05/pymotw-logging.html

"""

import logging

logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('This message comes from one module')
logger2.warning('And this message comes from another module')
