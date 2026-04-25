
def Help():
    while True:
        # Assuming 'andHelp' is defined somewhere in your code
        print('The options available are: \n')
        for i in andHelp:
            print(i)
        print('Type Q to Quit \n')

        x = input('What option do you choose: ').strip()
        print('\n')

        if x == 'Q':
            break
        elif x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        else:
            print("Invalid option. Please try again.")
