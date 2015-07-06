#!/usr/bin/env python

import re
import sys


# Start main
if __name__ == '__main__':
    try:
        fileName = sys.argv[1]
    except IndexError:
        print("Need a file name")
        sys.exit(1)
    else:
        fh = open(fileName, 'r')
        lines = fh.readlines()
        for line in lines:
            # Split lines on letters, numbers, and apostrophes
            # Hypenated words will be split
            wordList = re.split("[^\w']+", line.rstrip())
            # Shortening length by one so that we don't overrun the index
            # Also, this is preferred since we only want word pairs
            for i in range(len(wordList) - 1):
                print("{0:d}: {1} -> {2}".format(i, wordList[i],
                      wordList[i + 1]))
