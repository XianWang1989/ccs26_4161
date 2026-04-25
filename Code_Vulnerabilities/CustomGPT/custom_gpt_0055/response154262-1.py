
def Help():
    while True:
        x = input('What option do you choose (Manifest, Intent, or Q to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            print('Quitting...')
            break
        else:
            print('The options available are:\n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example usage of the Help function
andHelp = ['Manifest', 'Intent']
def Manifest():
    return "Manifest function executed."

def Intent():
    return "Intent function executed."

Help()
