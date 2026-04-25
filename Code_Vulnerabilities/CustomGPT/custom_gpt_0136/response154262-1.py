
def Help():
    while True:
        x = input('What option do you choose (Manifest/Intent/Q to Quit): ')
        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            print('Quitting...')
            break
        else:
            print('The options available are:')
            print('Manifest')
            print('Intent')
            print('Type Q to Quit')
            print('\n')

# Example usage (define Manifest and Intent functions)
def Manifest():
    print("Manifest function executed.")

def Intent():
    print("Intent function executed.")

# Start the helper
Help()
