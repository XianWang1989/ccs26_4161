
def Help():
    while True:
        x = input('What option do you choose (Type Q to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)

# Example usage:
andHelp = ['Manifest', 'Intent']
Help()
