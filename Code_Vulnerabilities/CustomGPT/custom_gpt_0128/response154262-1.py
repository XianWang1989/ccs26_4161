
def Help():
    while True:
        string = input('Enter Manifest or Intent (or Q to Quit): ')
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            break
        else:
            print('The options available are:\n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit\n')

# Example usage of the Help function.
Help()
