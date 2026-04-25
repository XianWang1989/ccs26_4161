
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are:\n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit\n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                # Update string with the new input 
                string = x  # Use the new input instead of calling Help recursively
