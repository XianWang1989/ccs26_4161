
def Help():
    while True:
        print('The options available are:')
        print('1. Manifest')
        print('2. Intent')
        print('Type Q to Quit')

        x = input('What option do you choose: ')
        print('\n')

        if x == 'Manifest':
            return Manifest()  # Call the Manifest function
        elif x == 'Intent':
            return Intent()  # Call the Intent function
        elif x == 'Q':
            break
        else:
            print('Invalid option, please try again.\n')

def Manifest():
    return "Manifest function executed."

def Intent():
    return "Intent function executed."

# Start the Help function
Help()
