
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
            # break is unnecessary here because return exits the function
        elif string == 'Intent':
            return Intent()
            # break is unnecessary here because return exits the function
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
                string = x  # Update string with the new input
