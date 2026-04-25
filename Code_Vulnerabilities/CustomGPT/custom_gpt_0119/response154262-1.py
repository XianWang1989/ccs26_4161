
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Ensure Manifest is defined elsewhere
        elif string == 'Intent':
            return Intent()     # Ensure Intent is defined elsewhere
        else:
            print('The options available are: \n')
            for i in andHelp:    # Ensure andHelp is defined
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update the string variable instead of calling Help again

# Example definitions for Manifest and Intent
def Manifest():
    return "Manifest function executed."

def Intent():
    return "Intent function executed."

# Example list for andHelp
andHelp = ["Manifest", "Intent"]
