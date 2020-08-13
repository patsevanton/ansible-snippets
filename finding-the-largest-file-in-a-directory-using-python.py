#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json

# Emtry JSON Data
data = []

# folder path input
path = "/var/log"

min_size = 524288000

# for storing size of each
# file
size = 0

# for storing the size of
# the largest file
max_size = 0

# for storing the path to the
# largest file
path_max_file =""

# walking through the entire folder,
# including subdirectories

for folder, subfolders, files in os.walk(path):

	# checking the size of each file
	for file in files:
		size = os.stat(os.path.join( folder, file )).st_size

		# updating maximum size
		if size>max_size and size>min_size:
			max_size = size
			path_max_file = os.path.join( folder, file )


data.append({'#LARGESTLOGFILE':path_max_file})
jsondata = json.dumps(data)

print json.dumps({"data": data})


