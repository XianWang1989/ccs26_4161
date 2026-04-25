
def Help():
    while True:
        # Display options
        print('The options available are: \n')
        for i in andHelp:
            print(i)
        print('Type Q to Quit \n')

        # User input
        x = input('What option do you choose: ')
        print('\n')

        if x == 'Q':
            break
        elif x == 'Manifest':
            return Manifest()  # Call Manifest function if needed
        elif x == 'Intent':
            return Intent()     # Call Intent function if needed
        else:
            print("Invalid option, please try again.\n")

# Assume `andHelp` is defined somewhere in your code
# Also, ensure that the Manifest and Intent functions are defined properly
