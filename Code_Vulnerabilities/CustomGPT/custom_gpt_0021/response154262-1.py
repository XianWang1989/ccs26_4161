
def Help():
    while True:
        string = input('What option do you choose (Manifest, Intent, or Q to quit): ')
        print('\n')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            break
        else:
            print('The options available are: \n')
            print('Intent')
            print('Manifest')
            print('Type Q to Quit \n')

# Example Manifest and Intent functions for context
def Manifest():
    print("Manifest function called.")

def Intent():
    print("Intent function called.")

# Call the Help function to start
Help()
