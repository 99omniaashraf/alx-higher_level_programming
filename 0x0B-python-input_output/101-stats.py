#!/usr/bin/python3
import sys
import io


dictstatus = {}
totalsize = 0
totalcount = 0
for line in sys.stdin:
    split = line.split
    status = split[-2]
    totalsize += int(split[-1])
    if status in dictstatus.keys():
        dictstatus[status] += 1
    else:
        dictstatus[status] = 1
    totalcount += 1
    if totalcount == 10:
        sortme = sorted(dictstatus.keys())
        print("File size:", totalsize)
        for keys in sortme:
            print("{}: {}".format(keys, dictstatus[keys]))
        totalcount = 0
        continue
