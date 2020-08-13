#!/usr/bin/env python

import mmap
import os
import re

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def tail(filename, n):
    """Returns last n lines from the filename. No exception handling"""
    size = os.path.getsize(filename)
    with open(filename, "rb") as f:
        # for Windows the mmap parameters are different
        fm = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
        try:
            for i in xrange(size - 1, -1, -1):
                if fm[i] == '\n':
                    n -= 1
                    if n == -1:
                        break
            return fm[i + 1 if i else 0:].splitlines()
        finally:
            fm.close()

for string in tail("/var/log/puppet/puppet.log", 20):
  # print(ansi_escape.sub('', string))
  if  'Error:' or 'Could not' in ansi_escape.sub('', string):
    print(ansi_escape.sub('', string))

