#!/usr/bin/env python

import re
import sys

wordDict = {}


def readFile(filename):
    fullText = []
    fh = open(filename, 'r')
    lines = fh.readlines()
    for line in lines:
        # Look for lines that either long enough to be part of a paragraph or
        # end in a period.
        if (len(line) > 50 or re.search("\.$", line.rstrip())):
            # Treat double hyphens as a space
            cleanLine = line.rstrip().replace("--", " ")
            # Split lines on letters, numbers, hyphens and apostrophes
            wordList = re.split("[^\w'-]+", cleanLine)
            fullText.extend(filter(None, wordList))

    return(fullText)


def buildDict(line):
    # Shortening length by two so that we don't overrun the index
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
        text = readFile(filename)
        buildDict(text)
