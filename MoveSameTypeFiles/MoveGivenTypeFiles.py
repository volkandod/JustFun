#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, hashlib
import subprocess as sp

if __name__ == '__main__':
    if len(sys.argv) != 4:  #The script must be called with three argument
        sys.stdout.write("Needs only threeo valid argument\n")
        sys.exit(1)
    Type = sys.argv[1]
    topdir = sys.argv[2]
    desdir = sys.argv[3]
    Type = '.' + Type
    print Type
    file_digests = {}
    for root, _, files in os.walk(topdir): #Finds all files in given directory
        for f in files:
            abs_path = os.path.join(root, f)
            if Type in abs_path:
                sp.call(['mv', abs_path, desdir]) 
