#!/usr/bin/python3
import sys
import logging

# Set logging level
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
# Create global donor list
donorList = [["Test User", 100]]


def getPromptInput():
    userInput = input('> ')
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
    userInput = getPromptInput().lower()

    if (userInput == 't'):
        print('Choose T')
        parseThankChoices()
    elif (userInput == 'r'):
        print('Choose R')
    elif (userInput == 'quit' or userInput == 'q'):
        print('Choose quit')
        sys.exit(0)
    else:
        logging.debug("Invalid entry")
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
        logging.debug('Choose list')
    elif (userInput == 'quit' or userInput == 'q'):
        logging.debug('Choose quit')
        return(0)
    else:
        # Name has been entered
        donorIndex = parseNameEntry(userInput)
        donorAmt = getDonationAmt(donorIndex)
        if (donorAmt > 0):
            logging.debug("Going to send note: " + str(donorAmt))
            sendNote(donorIndex, donorAmt)
    parseThankChoices()


def parseNameEntry(fullName):
    donorIndex = -1
    listLength = len(donorList)
    logging.debug("listLength: " + str(listLength))
    for i in range(listLength):
        logging.debug("Iterating: " + str(i))
        retName = donorList[i][0]
        if (retName == fullName):
            # Name Found
            logging.debug("Name Found: " + fullName + " at " + str(i))
            donorIndex = i
        else:
            logging.debug("No Match: " + fullName + "!=" + retName)
    if (donorIndex < 0):
        logging.debug("Name NOT Found: " + fullName)
        donorList.append([fullName, 0, 0])
        donorIndex = len(donorList) - 1
    return(donorIndex)


def getDonationAmt(donorIndex):
    print("Please enter a donation amount or 'quit':")
    userInput = getPromptInput()
    if (userInput == "quit" or userInput == 'q'):
        return(-1)
    else:
        donationAmt = int(userInput)
        donorList[donorIndex][1] += donationAmt
        return(donationAmt)


def sendNote(donorIndex, donorAmt):
    name = donorList[donorIndex][0]
    print("Dear " + name + ",")
    print("")
    print("Thank you so much for your kind donation of $", end="")
    print(str(donorAmt) + ". We here at the Foundation for Homeless ", end="")
    print("Whales greatly appreciate it. Your money will go towards ", end="")
    print("creating new oceans on the moon for whales to live in.", end="")
    print("")
    print("Thanks again,")
    print("")
    print("Jim Grant")
    print("")
    print("Director, F.H.W.")
    print("")
    print("Press Enter to Continue...")
    print("")
    getPromptInput()
    return(0)


# Start main
parseInitialChoices()
