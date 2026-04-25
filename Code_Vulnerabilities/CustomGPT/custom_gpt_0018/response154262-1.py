
def Help():
    while True:
        string = input('What option do you choose: ')
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
            print('Type Q to Quit \n')

# Assuming Manifest and Intent functions are defined,
# and 'andHelp' is a predefined list of options.
