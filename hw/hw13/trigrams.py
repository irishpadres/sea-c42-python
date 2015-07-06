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
            wordList = re.split("[^\w'-]+", line)
            for i in range(len(wordList)):
                if (wordList[i] == ''):
                    pass
                else:
                    print("{0:d}: {1}".format(i, repr(wordList[i])))
