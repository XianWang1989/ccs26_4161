
def Help():
    while True:
        x = input('What option do you choose (Manifest, Intent, or Q to quit): ')
        print('\n')
        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            print("Exiting...")
            break
        else:
            print('The options available are: ')
            print('Manifest')
            print('Intent')
            print('Type Q to Quit \n')

# Dummy functions to demonstrate functionality
def Manifest():
    return "Manifest function called."

def Intent():
    return "Intent function called."

# Call the Help function to start
Help()
