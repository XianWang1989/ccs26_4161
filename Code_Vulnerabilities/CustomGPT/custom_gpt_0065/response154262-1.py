
def Help():
    while True:
        print('The options available are: \n')
        for i in andHelp:
            print(i)
        print('Type Q to Quit \n')

        x = input('What option do you choose: ')
        print('\n')

        if x == 'Q':
            print('Goodbye!')
            break
        elif x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        else:
            print('Invalid choice, please try again.')

# Example usage
andHelp = ['Intent', 'Manifest']  # Define available options
Help()
