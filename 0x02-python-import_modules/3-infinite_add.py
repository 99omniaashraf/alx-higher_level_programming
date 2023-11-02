#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(argv)
    add = 0
    if num == 1:
        print("{:d}".format(add))
    else:
        for i in range(1, num):
            add += int(argv.__getitem__(i))
        print("{:d}".format(add))
