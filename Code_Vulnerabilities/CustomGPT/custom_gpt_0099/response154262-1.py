
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
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
                return Help(x)  # Return the result of the recursive call

# Example function definitions for Manifest and Intent
def Manifest():
    return "Manifest function executed."

def Intent():
    return "Intent function executed."

# Example list for options
andHelp = ['Intent', 'Manifest']
