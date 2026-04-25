
def Help():
    while True:
        x = input('What option do you choose (Manifest, Intent) or type Q to Quit: ').strip()
        print('\n')

        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            print('Exiting...')
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example usage:
# Define Manifest and Intent functions, and the andHelp variable
def Manifest():
    print("Manifest function executed.")

def Intent():
    print("Intent function executed.")

andHelp = ["Manifest", "Intent"]

Help()
