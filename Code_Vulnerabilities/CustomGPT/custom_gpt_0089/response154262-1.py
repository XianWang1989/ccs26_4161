
def Help():
    while True:
        x = input('What option do you choose: ')
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
            print('Type Q to Quit \n')

# Example implementations of Manifest and Intent for context
def Manifest():
    print("You chose Manifest.")

def Intent():
    print("You chose Intent.")

# Example options
andHelp = ['Manifest', 'Intent']
Help()
