
def Help():
    while True:
        x = input('What option do you choose (Type "Manifest", "Intent", or "Q" to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            print("Quitting...")
            break
        else:
            print('The options available are:\n')
            print('Manifest')
            print('Intent')
            print('Type Q to Quit\n')

# Example usage of Help: 
# Make sure to define Manifest() and Intent() functions before calling Help().
