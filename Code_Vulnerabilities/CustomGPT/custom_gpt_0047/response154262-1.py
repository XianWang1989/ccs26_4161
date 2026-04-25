
def Help():
    while True:
        string = input('What option do you choose (Manifest, Intent, or Q to Quit): ')
        print('\n')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)

# Assume Manifest and Intent are defined elsewhere
