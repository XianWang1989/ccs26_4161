
def Help():
    while True:
        x = input('What option do you choose (Type Q to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()  # Call Manifest function
        elif x == 'Intent':
            return Intent()  # Call Intent function
        elif x == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print()

# Sample usage of the Help function
def Manifest():
    print("You selected Manifest.")

def Intent():
    print("You selected Intent.")

andHelp = ["Manifest", "Intent"]  # Example options
Help()
