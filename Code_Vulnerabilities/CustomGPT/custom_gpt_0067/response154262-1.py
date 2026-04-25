
def Help():
    while True:
        x = input('What option do you choose (Manifest/Intent/Q): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()  # Assuming Manifest is defined elsewhere
        elif x == 'Intent':
            return Intent()  # Assuming Intent is defined elsewhere
        elif x == 'Q':
            print('Quitting...')
            break
        else:
            print('The options available are:')
            print('Manifest')
            print('Intent')
            print('Type Q to Quit \n')
