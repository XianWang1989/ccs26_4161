
def Help():
    while True:
        string = input('What do you choose: ')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            if string == 'Q':
                break
