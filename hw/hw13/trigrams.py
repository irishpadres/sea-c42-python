#!/usr/bin/env python

import re
import sys
import random


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
    wordDict = {}
    # Shortening length by two so that we don't overrun the index
    # Also, this is preferred since we only want to evaluate the final
    # three words
    for i in range(len(wordList) - 2):
        curWord = wordList[i]
        nextWord = wordList[i + 1]
        lastWord = wordList[i + 2]
        # if (curWord.istitle()):
        #    if ((curWord.lower(), nextWord) in wordDict):
        #        print("{0} and {1}".format(curWord, curWord.lower()))
        wordDict.setdefault((curWord, nextWord), []).append(lastWord)
    return(wordDict)


def writeStory(wordDict):
    wordTuple = random.choice(list(wordDict.keys()))
    # Create 6 to 8 paragraphs
    for paraNum in range(0, random.randrange(6, 9)):
        # Create 6 to 8 sentances
        for sentNum in range(0, random.randrange(6, 9)):
            # Create 10 to 15 words per sentance
            for wordNum in range(0, random.randrange(10, 16)):
                priWord = wordTuple[0]
                secWord = wordTuple[1]
                terWord = random.choice(wordDict[wordTuple])
                print("{0} {1} {2}".format(priWord, secWord, terWord))
                wordTuple = (secWord, terWord)


# Start main
if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Need a file name")
        sys.exit(1)
    else:
        text = readFile(filename)
        wordDict = buildDict(text)
        story = writeStory(wordDict)
        # print(story)
