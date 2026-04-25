
def Help():
    while True:
        string = input('What option do you choose (Manifest/Intent/Q to Quit): ')
        print('\n')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            break
        else:
            print('The options available are:\n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit\n')

# Example functions for Manifest and Intent
def Manifest():
    print("Manifest function executed.")
    # Your logic here

def Intent():
    print("Intent function executed.")
    # Your logic here

# Dummy list for demonstration
andHelp = ['Manifest', 'Intent']
