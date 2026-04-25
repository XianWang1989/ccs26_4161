
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are:')
            for i in andHelp:  # Ensure andHelp is defined elsewhere
                print(i)
            print('Type Q to Quit')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update the string variable to the new input

# Example definitions for Manifest and Intent
def Manifest():
    print("You've chosen Manifest.")
    return

def Intent():
    print("You've chosen Intent.")
    return

# Example list of help options
andHelp = ['Intent', 'Manifest']
