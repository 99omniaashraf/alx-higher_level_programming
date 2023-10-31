#!/usr/bin/python3
for i in range(0, 10):
    for a in range(i, 10):
        if i < a:
            print("{:d}{:d}".format(i, a), 
                end="\n" if i == 8 and a == 9 else ", ")
