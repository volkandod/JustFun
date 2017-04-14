#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
import subprocess as sp

if __name__ == '__main__':
    topdir = sys.argv[1]
    for root,_, files in os.walk(topdir):
        for f in files:
            if "epub" in os.path.join(root,f):
                EpubList = os.path.join(root,f)
                TmpList = EpubList[:-4]
                MobiList = TmpList + "mobi"
                os.system("ebook-convert \"" + EpubList + "\" \"" + MobiList + "\"")
                sp.call(['rm', EpubList])

