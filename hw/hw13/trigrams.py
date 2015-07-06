#!/usr/bin/env python

import re
import sys

wordDict = {}


def readFile(filename):
    fh = open(filename, 'r')
    lines = fh.readlines()
    for line in lines:
        strpdLine = line.rstrip()
        if (len(strpdLine) > 50 or re.search("\.$", strpdLine)):
            print(strpdLine)
        # Split lines on letters, numbers, and apostrophes
        # Hypenated words will be split
        wordList = re.split("[^\w']+", strpdLine)
        # Shortening length by one so that we don't overrun the index
        # Also, this is preferred since we only want word pairs
        for i in range(len(wordList) - 1):
            curWord = wordList[i]
            nextWord = wordList[i + 1]
            # print("{0:d}: {1} -> {2}".format(i, curWord, nextWord))
            # wordDict[(curWord, nextWord)]


# Start main
if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Need a file name")
        sys.exit(1)
    else:
        readFile(filename)
