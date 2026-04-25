
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are: ')
            for i in andHelp:
                print(i)
            print('Type Q to Quit ')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                # Check the new input without recursively calling Help
                string = x
