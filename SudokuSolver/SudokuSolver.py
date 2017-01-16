#!/usr/bin/env python
# -*- coding: utf-8 -*-

def CrossProduct(valA, valB):
    tmp = []
    for i in range (0, len(valA)):
        for j in range (0, len(valB)):
            tmp.append(valA[i] + valB[j])
    return tmp
rows = cols = "123456789"

Squares = CrossProduct(rows, cols)
Column  = ([CrossProduct(rows, c) for c in cols])
Row     = ([CrossProduct(r, cols) for r in rows])
Group   = ([CrossProduct(r,s) for r in ('123','456','789') for s in ('123', '456', '789')])
Unit    = Column + Row + Group
Peer    = dict((s,sum([u for u in Unit if s in u],[])) for s in Squares)
Peers   = {}
Keys    = []

#Create Squares Dic
for s in Squares:
    for p in Peer[s]:
        if p not in s:
            try:
                if p not in Peers[s]:
                    tmpList = Peers[s]
                    tmpList.append(p)
            except:
                Peers[s] = [p]

#Create Initial Dic by using input
def ReadPuzzle(Puzzle):
    val = [c for c in Puzzle]
    return dict(zip(Squares,val))

def PrintSudoku(Tbl):
    width =  + max(len(Tbl[k]) for k in Squares)
    line = '+'.join(['-'*(width*5)]*3)
    for r in rows:
        print ''.join(Tbl[r+c].center(width)+('|' if c in '36' else ' ') for c in cols)
        if r in '36':
            print line

#Put value into the Tbl[key] 
def Put(Tbl, key, value):
    if len(Tbl[key]) == 1:
        return Tbl

    ToBeDeleted = Tbl[key].replace(value,'')
    if all(Remove(Tbl,key,t) for t in ToBeDeleted):
        return Tbl
    else:
        return False

#Remove value from Tbl[key]
def Remove(Tbl, key, value):
    if value in Tbl[key]:
        if len(Tbl[key]) == 1:
            return False
        Tbl[key] = Tbl[key].replace(value,'')
        if len(Tbl[key]) == 1:
            new_value = Tbl[key]
            if not all(Remove(Tbl, p, new_value) for p in Peers[key]):
                return False
        #Scan rows columns and groups of value, if there is one key include
        #value than put that value into key
        for u in Unit:
            if key in u:
                Keys = [s for s in u if value in Tbl[s]]

                if len(Keys) == 0:
                    return False
                elif len(Keys) == 1:
                    if not Put(Tbl,Keys[0],value):
                        return False
                del Keys[:]
        return Tbl
    else:
        return Tbl

#This function is used for recursively calls
def rec(seq):
    for e in seq:
        if e:
            return e
    return False

def Try(Tbl):
    if Tbl is False:
        return False
    if all(len(Tbl[k]) == 1 for k in Squares):
        return Tbl #Solved the puzzle

    #If the puzzle cannot be solved then try to solve with a possible value
    n,s = min((len(Tbl[key]),key) for key in Squares if len(Tbl[key]) > 1)

    return rec(Try(Put(Tbl.copy(),s, value)) for value in Tbl[s])


Table = dict((s, '123456789') for s in Squares)
Puzzle = '800000000003600000070090200050007000000045700000100030001000068008500010090000400'

Puzzle='080070400007019003100000080030000000690030017000000020010000004400560100005020030'
for k,v in ReadPuzzle(Puzzle).items():
    if '0' not in v:
        Put(Table, k, v)

PrintSudoku(Try(Table))
