
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Assumes Manifest() is defined elsewhere
        elif string == 'Intent':
            return Intent()  # Assumes Intent() is defined elsewhere
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                # Update `string` variable to the new input
                string = x

# Example definitions for Manifest and Intent
def Manifest():
    return "Manifest function executed."

def Intent():
    return "Intent function executed."

# Example list for options
andHelp = ['Intent', 'Manifest']
