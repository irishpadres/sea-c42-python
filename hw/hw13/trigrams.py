#!/usr/bin/env python

import re
import sys

wordDict = {}


def readFile(filename):
    fh = open(filename, 'r')
    lines = fh.readlines()
    for line in lines:
        # Treat double hyphens as a space
        cleanLine = line.rstrip().replace("--", " ")
        if (len(cleanLine) > 50 or re.search("\.$", cleanLine)):
            print(cleanLine)
            buildDict(cleanLine)


def buildDict(line):
    # Split lines on letters, numbers, and apostrophes
    # Hypenated words will be split
    wordList = re.split("[^\w']+", line)
    # Shortening length by one so that we don't overrun the index
    # Also, this is preferred since we only want to evaluate the final
    # three words
    for i in range(len(wordList) - 2):
        curWord = wordList[i]
        nextWord = wordList[i + 1]
        lastWord = wordList[i + 2]
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
