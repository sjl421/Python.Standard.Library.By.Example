#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Writing data to a new archive with writestr().
"""

import time
import zipfile
from zipfile_infolist import print_info

msg = 'This data did not exist in a file.'

with zipfile.ZipFile('writestr_zipinfo.zip', 
                     mode='w',
                     ) as zf:
    info = zipfile.ZipInfo('from_string.txt', 
                           date_time=time.localtime(time.time()),
                           )
    info.compress_type=zipfile.ZIP_DEFLATED
    info.comment='Remarks go here'
    info.create_system=0
    zf.writestr(info, msg)

print_info('writestr_zipinfo.zip')
