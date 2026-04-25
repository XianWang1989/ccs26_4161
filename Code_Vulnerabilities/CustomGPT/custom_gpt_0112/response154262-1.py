
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Assume Manifest() is defined elsewhere
        elif string == 'Intent':
            return Intent()  # Assume Intent() is defined elsewhere
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assume andHelp is defined elsewhere
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                print("Exiting...")
                break
            else:
                string = x  # Update the string to the new input
