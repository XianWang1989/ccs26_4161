
def Help():
    while True:
        string = input('What option do you choose: ')
        print('\n')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            print("Quitting...")
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example usage, assuming Manifest and Intent functions are defined:
# Help()
