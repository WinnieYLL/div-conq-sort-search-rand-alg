# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 15:55:17 2020

@author: winni
"""

import numpy as np

# Import data

data_list = []
filepath = "kargerMinCut.txt"
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       data_list.append(np.fromstring(line.strip(), int, -1, '\t').tolist())
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
       
while len(data_list) > 2
    # Randomly choose two rows to merge

    # === Process new row ===
    # Combine connections of the rows

    # Rename row and remove row

    # Remove duplicate connections in new row

    # === Process other rows ===
    # Merge connections containing nodes in new row

    # Remove duplicates

# Look up original data to find size of cut


       