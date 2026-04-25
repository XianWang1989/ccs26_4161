
def Help():
    while True:
        x = input('What option do you choose (Manifest, Intent, Q to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()  # Call Manifest function
        elif x == 'Intent':
            return Intent()  # Call Intent function
        elif x == 'Q':
            print("Exiting...")
            break
        else:
            print('The options available are:')
            print('Manifest')
            print('Intent')
            print('Type Q to Quit \n')

# Assuming Manifest and Intent are defined elsewhere
def Manifest():
    print("You chose Manifest!")

def Intent():
    print("You chose Intent!")

# Call the help function
Help()
