#!/usr/bin/python3
import sys


def getPromptInput():
    userInput = input('> ').lower()
    return(userInput)


def parseInitialChoices():
    '''This will parse the initial options given to the user.  It is intended
    to be the first function called and be the first level of user input.

    Args:
        None

    Returns:
        None
    '''
    print('Welcome to Mailroom Madness')
    print('Choose from the following:')
    print('T - Send a (T)hank You')
    print('R - Create a (R)eport')
    print('quit - Quit the program')
    userInput = getPromptInput()

    if (userInput == 't'):
        print('Choose T')
        parseThankChoices()
    elif (userInput == 'r'):
        print('Choose R')
    elif (userInput == 'quit' or userInput == 'q'):
        print('Choose quit')
        sys.exit(0)
    else:
        print("Invalid entry")
    parseInitialChoices()


def parseThankChoices():
    '''This will parse the Send a Thank You options given to the user.  It is
    intended to be the first function called and be the first level of user
    input.

    Args:
        None

    Returns:
        None
    '''
    print('Please enter a name, or choose from the following:')
    print('list - Print a list of previous donors')
    print('quit - Return to main menu')
    userInput = getPromptInput()

    if (userInput == 'list'):
        print('Choose list')
    elif (userInput == 'quit'):
        print('Choose quit')
        return(0)
    else:
        print('Invalid entry')
    parseThankChoices()


# Start main
parseInitialChoices()
