#!/usr/bin/env python

import glob
import os
os.chdir("/etc/td-agent/conf.d/")
for file in glob.glob('*'):
    with open(file) as openfile:
        for line in openfile:
            for part in line.split():
                if "/var/log" in part:
                    bashCommand = "lsof {0}".format(part)
                    if len(glob.glob(part)) > 1:
                        print(glob.glob(part))

