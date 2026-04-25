
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Properly handle the return
        elif string == 'Intent':
            return Intent()  # Properly handle the return
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                # Use the new input for the next iteration of the loop
                string = x  # This updates `string` instead of calling Help again
