
def Help():
    while True:
        x = input('What option do you choose (Manifest, Intent, Q to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()  # Call the Manifest function
        elif x == 'Intent':
            return Intent()  # Call the Intent function
        elif x == 'Q':
            print("Quitting...")  # Handle quitting
            break
        else:
            print('Invalid option. The options available are:\n')
            for i in andHelp:  # Assuming andHelp is defined elsewhere
                print(i)
            print('Type Q to Quit \n')

# Example definitions for Manifest and Intent functions
def Manifest():
    print("Manifest function executed.")

def Intent():
    print("Intent function executed.")

# Assuming `andHelp` contains the options
andHelp = ['Manifest', 'Intent']
Help()
