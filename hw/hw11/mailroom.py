#!/usr/bin/python3
import sys
import logging

# Set logging level
logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)
# Create global donor list
donorList = {}
# Max name length
maxNameLen = 0
# Max amount length
maxAmtLen = 0
# Max quantity length
maxQtyLen = 0


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
        parseThankChoices()
    elif (userInput == 'r'):
        printReport()
    elif (userInput == 'quit' or userInput == 'q'):
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
        printReport()
    elif (userInput == 'quit' or userInput == 'q'):
        logging.debug('Choose quit')
        sys.exit(0)
    else:
        # Name has been entered
        # donorIndex = parseNameEntry(userInput)
        fullName = userInput
        donorAmt = getDonationAmt(fullName)
        if (donorAmt > 0):
            logging.debug("Going to send note: " + str(donorAmt))
            returnCode = sendNote(fullName, donorAmt)
            if (returnCode < 0):
                return(0)
    parseThankChoices()


# def parseNameEntry(fullName):
#    listLength = len(donorList)
#    logging.debug("listLength: " + str(listLength))
#    for i in range(listLength):
#        logging.debug("Iterating: " + str(i))
#        retName = donorList[i][0]
#        if (retName == fullName):
#            # Name Found
#            logging.debug("Name Found: " + fullName + " at " + str(i))
#            donorIndex = i
#        else:
#            logging.debug("No Match: " + fullName + "!=" + retName)
#    if (donorIndex < 0):
#        global maxNameLen
#        logging.debug("Name NOT Found: " + fullName)
#        donorList.append([fullName, 0, 0])
#        donorIndex = len(donorList) - 1
#        if (len(fullName) > maxNameLen):
#            maxNameLen = len(fullName)
#    return(donorIndex)


def getDonationAmt(donorName):
    print("Please enter a donation amount or 'quit':")
    userInput = getPromptInput()
    if (userInput == "quit" or userInput == 'q'):
        return(-1)
    else:
        global maxNameLen
        global maxAmtLen
        global maxQtyLen

        donationAmt = float(userInput)

        if (donorName not in donorList):
            donorList[donorName] = []
        donorList[donorName].append(donationAmt)

        nameLen = len(donorName)
        if (nameLen > maxNameLen):
            maxNameLen = nameLen

        amtLen = len(str(round(donationAmt)))
        if (amtLen > maxAmtLen):
            maxAmtLen = amtLen

        qtyLen = len(str(len(donorList[donorName])))
        if (qtyLen > maxQtyLen):
            maxQtyLen = qtyLen
        return(donationAmt)


def sendNote(name, donorAmt):
    print("Dear " + name + ",")
    print("")
    print("Thank you so much for your kind donation of $", end="")
    print('{0:0.2f}. We here at the Foundation'.format(donorAmt))
    print("for Homeless Whales greatly appreciate it. Your money will go")
    print("towards creating new oceans on the moon for whales to live in.")
    print("")
    print("Thanks again,")
    print("")
    print("Jim Grant")
    print("")
    print("Director, F.H.W.")
    print("")
    print("Press Enter to Continue...")
    print("")
    userInput = getPromptInput()
    if (userInput == 'quit'):
        sys.exit(0)
    else:
        return(0)


def printReport():
    print('{0:^{1}} | {2:^{3}} | {4:^{5}} | {6}'.format(
          'Name', maxNameLen, 'Total', maxAmtLen + 4, '#', maxQtyLen,
          'Average'))
    for name in donorList.keys():
        logging.debug(name)
        total = 0
        for amt in donorList[name]:
            total += amt
        qty = len(donorList[name])
        print('{0:<{1}} | ${2:{3}.2f} | {4} | ${5:0.2f}'.format(
              name, maxNameLen, total, maxAmtLen + 3, qty, total / qty))


# Start main
if __name__ == '__main__':
    parseInitialChoices()
