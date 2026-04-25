
def Help():
    while True:
        string = input('What option do you choose: ')
        print('\n')
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            print('Quitting...')
            break
        else:
            print('The options available are:')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Call this function to start
Help()
