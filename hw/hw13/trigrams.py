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


def buildDict(wordList):
    # Shortening length by two so that we don't overrun the index
    # Also, this is preferred since we only want to evaluate the final
    # three words
    for i in range(len(wordList) - 2):
        curWord = wordList[i]
        nextWord = wordList[i + 1]
        lastWord = wordList[i + 2]
        if (curWord.istitle()):
            if ((curWord.lower(), nextWord) in wordDict):
                print("{0} and {1}".format(curWord, curWord.lower()))
        wordDict.setdefault((curWord, nextWord), []).append(lastWord)
    return(0)


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
        for pair in wordDict.keys():
            print("{0}: {1}".format(pair, wordDict[pair]))
        # print(wordDict)
