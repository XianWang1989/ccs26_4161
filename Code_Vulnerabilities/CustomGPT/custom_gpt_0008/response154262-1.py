
def Help():
    while True:
        x = input('What option do you choose (Manifest or Intent)? Or type Q to Quit: ')
        print('\n')

        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Assuming Manifest and Intent functions are defined and andHelp is a list of options.
