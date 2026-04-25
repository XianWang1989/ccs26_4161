
def Help():
    while True:
        x = input('What option do you choose (Manifest, Intent, Q to Quit): ')
        print('\n')
        if x == 'Manifest':
            return Manifest()  # or appropriate action for Manifest
        elif x == 'Intent':
            return Intent()  # or appropriate action for Intent
        elif x == 'Q':
            print('Quitting...')
            break
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assume andHelp is defined
                print(i)
            print('Type Q to Quit \n')

# Example definitions for Manifest and Intent
def Manifest():
    print("You chose Manifest.")

def Intent():
    print("You chose Intent.")

# Example list for andHelp
andHelp = ["Intent", "Manifest"]
