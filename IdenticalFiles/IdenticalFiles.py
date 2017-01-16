#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, hashlib
import subprocess as sp

def md5(fname):             #Get hash value of given file
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if __name__ == '__main__':
    if len(sys.argv) != 2:  #The script must be call with one argument
        sys.stdout.write("Needs only one valid argument\n")
        sys.exit(1)
    topdir = sys.argv[1]
    cntt = 0
    file_digests = {}
    for root, _, files in os.walk(topdir): #Finds all files in given directory
        for f in files:
            abs_path = os.path.join(root, f)
            hsh = md5(abs_path)
            try:
                dups = file_digests[hsh]    #if same hash value exists in dictionary, append new file as value
                dups.append(abs_path)
            except KeyError as e:
                file_digests[hsh] = [abs_path]  #write new hash and value to dictionary
    cnt = 1
    for key in file_digests.keys():
        cnt = 1
        if len(file_digests[key]) > 1:  #Then that hash key has more than one values

            for value in file_digests[key]:
                print str(cnt) + ' - ' + file_digests[key][cnt - 1]   #Print values to console
                cnt = cnt + 1
            delitem = raw_input('Select files to be deleted (seperated by ,)\nEnter 0 to keep all files in your system :  ')
#           delitem = '2'
            print '\n\n'
            sep = delitem.split(',')
            if '0' not in sep:
                for val in sep:
                    sp.call(['rm','-rf', file_digests[key][int(val) - 1]]) #Remove selected files
                    cntt = cntt + 1
    print 'Number of deleted items = ' + str(cntt)
