
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # A placeholder for your Manifest function
        elif string == 'Intent':
            return Intent()     # A placeholder for your Intent function
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
                # Assign the new choice to 'string' and continue looping
                string = x  
