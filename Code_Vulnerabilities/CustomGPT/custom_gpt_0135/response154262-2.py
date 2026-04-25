
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Assuming Manifest() is defined
        elif string == 'Intent':
            return Intent()  # Assuming Intent() is defined
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assuming andHelp is defined
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update the string variable to the new input
