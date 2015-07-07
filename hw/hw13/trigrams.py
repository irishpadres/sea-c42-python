#!/usr/bin/env python

import re
import sys
import random


sampleText = [
    "One night--it was on the twentieth of March, 1888--I was",
    "returning from a journey to a patient (for I had now returned to",
    "civil practice), when my way led me through Baker Street. As I",
    "passed the well-remembered door, which must always be associated",
    "in my mind with my wooing, and with the dark incidents of the",
    "Study in Scarlet, I was seized with a keen desire to see Holmes",
    "again, and to know how he was employing his extraordinary powers.",
    "His rooms were brilliantly lit, and, even as I looked up, I saw",
    "his tall, spare figure pass twice in a dark silhouette against",
    "the blind. He was pacing the room swiftly, eagerly, with his head",
    "sunk upon his chest and his hands clasped behind him. To me, who",
    "knew his every mood and habit, his attitude and manner told their",
    "own story. He was at work again. He had risen out of his",
    "drug-created dreams and was hot upon the scent of some new",
    "problem. I rang the bell and was shown up to the chamber which",
    "had formerly been in part my own."
    ]


def readFile(filename):
    fh = open(filename, 'r')
    lines = fh.readlines()
    return lines


def cleanText(lines):
    fullText = []
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
    # Create 3 to 4 paragraphs
    for paraNum in range(0, random.randrange(3, 5)):
        # Create 6 to 8 sentances
        for sentNum in range(0, random.randrange(6, 9)):
            wordTuple = random.choice(list(wordDict))
            while wordTuple in wordDict:
                priWord = wordTuple[0]
                secWord = wordTuple[1]
                terWord = random.choice(wordDict[wordTuple])
                print("{0}, {1}: {2} {3} {4}".format(paraNum, sentNum, priWord,
                      secWord, terWord))
                wordTuple = (secWord, terWord)


# Start main
if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print("No file name given...using sample text")
        lines = sampleText
    else:
        lines = readFile(filename)
    text = cleanText(lines)
    wordDict = buildDict(text)
    story = writeStory(wordDict)
    # print(story)
