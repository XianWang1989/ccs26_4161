
def Help():
    while True:
        x = input('What option do you choose (Manifest, Intent, Q to Quit): ')
        print('\n')
        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            print('Quitting...')
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example function stubs for Manifest and Intent
def Manifest():
    return "Manifest function called."

def Intent():
    return "Intent function called."

# Example usage
andHelp = ['Intent', 'Manifest']
Help()
