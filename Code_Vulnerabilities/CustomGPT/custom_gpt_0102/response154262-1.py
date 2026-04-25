
def Help():
    while True:
        # Prompt the user for input
        x = input('What option do you choose (Manifest, Intent, Q to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()  # Call your Manifest function
        elif x == 'Intent':
            return Intent()     # Call your Intent function
        elif x == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example functions
def Manifest():
    print("Manifest function invoked.")

def Intent():
    print("Intent function invoked.")

andHelp = ['Manifest', 'Intent']
Help()
