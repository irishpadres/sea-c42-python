#!/usr/bin/python3
import sys


def showInputChoices():
    print('Welcome to Mailroom Madness')
    print('Choose from the following:')
    print('T - Send a (T)hank You')
    print('R - Create a (R)eport')
    print('quit - Quit the program')

    userInput = input('> ')

    return(userInput)


def parseInputChoices():
    userInput = showInputChoices()
    if (userInput == 'T'):
        print('Choose T')
    elif (userInput == 'R'):
        print('Choose R')
    elif (userInput == 'quit'):
        print('Choose quit')
        sys.exit(0)
    else:
        parseInputChoices()

parseInputChoices()
