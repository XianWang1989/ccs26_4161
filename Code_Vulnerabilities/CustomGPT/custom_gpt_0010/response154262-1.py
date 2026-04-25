
def Help():
    while True:
        x = input('What option do you choose (Manifest, Intent, or Q to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            print("Quitting.")
            break
        else:
            print('The options available are: \n')
            # Assuming andHelp is defined somewhere in your code
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Assuming Manifest and Intent are defined functions
def Manifest():
    print("Manifest chosen.")

def Intent():
    print("Intent chosen.")

# Example list for options
andHelp = ["Manifest", "Intent"]

# Start the help function
Help()
