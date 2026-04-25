
def Help():
    while True:
        x = input('What option do you choose: ')
        print('\n')

        if x == 'Q':
            break
        elif x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example Manifest and Intent functions
def Manifest():
    print("You chose Manifest")

def Intent():
    print("You chose Intent")

# Sample list for demonstration
andHelp = ['Manifest', 'Intent']
