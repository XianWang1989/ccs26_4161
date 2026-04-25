
def Help():
    while True:
        x = input('What option do you choose (Manifest/Intent/Q to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            print('Goodbye!')
            break
        else:
            print('The options available are:')
            print('Manifest')
            print('Intent')
            print('Type Q to Quit')


# Example Manifest and Intent functions for demonstration
def Manifest():
    print("Manifest function called.")
    return

def Intent():
    print("Intent function called.")
    return

# Call the Help function to start
Help()
